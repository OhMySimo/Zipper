import os
import zipfile
import time
from isal import isal_zlib as zlib  # noqa: F401  — ISAL acceleration

from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn, MofNCompleteColumn, Progress,
    SpinnerColumn, TaskProgressColumn,
    TextColumn, TimeElapsedColumn, TimeRemainingColumn,
)
from rich.prompt import Prompt
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

console = Console()

BANNER = """
 ███████╗██╗██████╗ ██████╗ ███████╗██████╗ 
 ╚══███╔╝██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
   ███╔╝ ██║██████╔╝██████╔╝█████╗  ██████╔╝
  ███╔╝  ██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
 ███████╗██║██║     ██║     ███████╗██║  ██║
 ╚══════╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
"""


def print_banner():
    console.print()
    console.print(Align.center(Text(BANNER, style="bold magenta")))
    console.print(
        Align.center(
            Text("◈  Fast ZIP Packer — ISAL Accelerated  ◈", style="bold bright_white")
        )
    )
    console.print()


def ask_config() -> tuple[str, str]:
    """Interactively ask the user for folder and output zip name."""
    console.print(
        Panel(
            "[dim]Inserisci i parametri per avviare la compressione.[/dim]",
            title="[bold magenta]⚙  Setup[/bold magenta]",
            border_style="magenta",
            box=box.ROUNDED,
            expand=False,
        )
    )
    console.print()

    source_dir = Prompt.ask(
        "  [bold magenta]📁 Cartella da zippare[/bold magenta]"
    ).strip()

    default_zip = os.path.basename(source_dir.rstrip("/\\")) + ".zip"
    output_zip = Prompt.ask(
        f"  [bold magenta]📦 Nome file output[/bold magenta]",
        default=default_zip,
    ).strip()

    console.print()
    return source_dir, output_zip


def collect_files(source_dir: str) -> list[tuple[str, str]]:
    """Return list of (absolute_path, archive_name) pairs."""
    pairs = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            abs_path = os.path.join(root, file)
            arcname  = os.path.relpath(abs_path, source_dir)
            pairs.append((abs_path, arcname))
    return sorted(pairs, key=lambda x: x[1])


def print_preview(source_dir: str, output_zip: str, file_count: int):
    table = Table(box=box.ROUNDED, show_header=False, border_style="magenta", padding=(0, 2))
    table.add_column(style="dim magenta", justify="right")
    table.add_column(style="bright_white")

    total_bytes = sum(
        os.path.getsize(os.path.join(r, f))
        for r, _, fs in os.walk(source_dir) for f in fs
    )

    table.add_row("Sorgente",       f"[bold]{source_dir}[/bold]")
    table.add_row("Output",         f"[bold]{output_zip}[/bold]")
    table.add_row("File trovati",   f"[bold yellow]{file_count:,}[/bold yellow]")
    table.add_row("Dimensione tot.",f"[bold]{total_bytes / (1024**2):.2f} MB[/bold]")
    table.add_row("Compressione",   "[bold green]DEFLATE lvl 1 — ISAL[/bold green]")

    console.print(
        Panel(table, title="[bold magenta]📋  Riepilogo Pre-Compressione[/bold magenta]",
              border_style="magenta", box=box.ROUNDED, expand=False)
    )
    console.print()


def fast_zip(source_dir: str, output_zip: str):
    print_banner()

    # ── Validation ─────────────────────────────────────────────────────────────
    source_dir, output_zip = ask_config()

    if not os.path.isdir(source_dir):
        console.print(
            Panel(f"[bold red]✗  Cartella non trovata:[/bold red] [red]{source_dir}[/red]",
                  border_style="red", box=box.ROUNDED)
        )
        return

    files = collect_files(source_dir)
    if not files:
        console.print(
            Panel("[bold yellow]⚠  Nessun file trovato nella cartella.[/bold yellow]",
                  border_style="yellow", box=box.ROUNDED)
        )
        return

    print_preview(source_dir, output_zip, len(files))

    # ── Compression ────────────────────────────────────────────────────────────
    errors       = []
    success_count = 0
    start_time   = time.perf_counter()

    progress = Progress(
        SpinnerColumn(spinner_name="dots2", style="magenta"),
        TextColumn("[bold magenta]{task.description}[/bold magenta]"),
        BarColumn(bar_width=34, style="magenta", complete_style="bright_magenta", finished_style="green"),
        TaskProgressColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        TextColumn("ETA"),
        TimeRemainingColumn(),
        console=console,
        transient=False,
    )

    with progress:
        task = progress.add_task("Compressione in corso...", total=len(files))

        with zipfile.ZipFile(output_zip, "w",
                             compression=zipfile.ZIP_DEFLATED,
                             compresslevel=1) as zipf:
            for abs_path, arcname in files:
                progress.update(task, description=f"[magenta]↪[/magenta] [dim]{arcname}[/dim]")
                try:
                    zipf.write(abs_path, arcname)
                    success_count += 1
                except Exception as exc:
                    errors.append((arcname, str(exc)))
                    progress.console.print(
                        f"  [bold red]✗[/bold red] [red]{arcname}[/red] — [dim]{exc}[/dim]"
                    )
                progress.advance(task)

        progress.update(task, description="[green]✔  Completato[/green]")

    # ── Summary ────────────────────────────────────────────────────────────────
    elapsed   = time.perf_counter() - start_time
    zip_size  = os.path.getsize(output_zip) / (1024 ** 2)

    console.print()
    console.print(Rule("[bold magenta]Riepilogo[/bold magenta]", style="magenta"))
    console.print()

    summary = Table(box=box.SIMPLE_HEAD, border_style="magenta",
                    show_header=False, padding=(0, 3))
    summary.add_column(justify="left",  style="dim")
    summary.add_column(justify="right", style="bold bright_white")

    summary.add_row("File processati",   str(len(files)))
    summary.add_row(
        "[green]✔  Aggiunti[/green]",
        f"[bold green]{success_count}[/bold green]"
    )
    summary.add_row(
        "[red]✗  Errori[/red]" if errors else "Errori",
        f"[bold red]{len(errors)}[/bold red]" if errors else f"[dim]0[/dim]"
    )
    summary.add_row("Dimensione ZIP",   f"{zip_size:.2f} MB")
    summary.add_row("Tempo totale",     f"{elapsed:.2f}s")
    summary.add_row("Velocità media",   f"{(zip_size / elapsed):.2f} MB/s")
    summary.add_row("Output",           output_zip)

    console.print(Align.center(summary))

    if errors:
        console.print()
        err_table = Table(
            title="[bold red]File con errori[/bold red]",
            box=box.ROUNDED, border_style="red",
            show_header=True, header_style="bold red",
        )
        err_table.add_column("File",   style="red")
        err_table.add_column("Errore", style="dim")
        for fname, msg in errors:
            err_table.add_row(fname, msg)
        console.print(err_table)

    console.print()
    if not errors:
        console.print(
            Align.center(
                Panel(
                    f"[bold green]  ZIP creato con successo! 🎉  →  [white]{output_zip}[/white][/bold green]",
                    border_style="green", box=box.ROUNDED, expand=False
                )
            )
        )
    else:
        console.print(
            Align.center(
                Panel(
                    f"[yellow]ZIP creato con [bold]{len(errors)}[/bold] errore/i.[/yellow]",
                    border_style="yellow", box=box.ROUNDED, expand=False
                )
            )
        )
    console.print()


if __name__ == "__main__":
    fast_zip("", "")   # args are ignored — config is collected interactively
