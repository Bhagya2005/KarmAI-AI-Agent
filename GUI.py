from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import threading
import sys
from Agents.OverallAgent import MasterAgent

class TerminalCLI:
    def __init__(self):
        self.console = Console()
        self.original_stdout = sys.stdout  # Store original stdout

    def display_header(self):
        """Displays the header panel with AI assistant name."""
        header = Panel("💡 KarmAI - AI Assistant\n👨‍💻 Developed by Bhagya Nitinkumar Patel", style="bold blue")
        self.console.print(header)
        self.console.print("[bold green]Hello, I am KarmAI. How may I help you?[/bold green]")
        self.console.print("[bold yellow]Type your query below or type 'exit' to quit.[/bold yellow]\n")

    def run(self):
        """Starts the CLI loop."""
        self.display_header()

        while True:
            query = Prompt.ask("[bold yellow]> Type your query[/bold yellow]")
            if query.lower() == "exit":
                self.console.print("[bold red]Exiting KarmAI. Goodbye![/bold red] 👋")
                break
            self.console.print(f"[bold blue]> {query}[/bold blue]\n")
            threading.Thread(target=self.run_operator, args=(query,), daemon=True).start()

    def run_operator(self, query):
        """Runs the AI processing in a separate thread."""
        sys.stdout = self  # Redirect stdout
        self.operator(query)
        sys.stdout = self.original_stdout  # Restore stdout

    def operator(self, query):
        """Calls the MasterAgent to process the query."""
        master = MasterAgent()
        master.agent_res(query)
        self.console.print("[bold green]✔ Task completed.[/bold green]")

    def write(self, message):
        """Writes output to the CLI without recursion issues."""
        if message.strip():  # Avoid printing empty lines
            self.original_stdout.write(message)  # Use original stdout instead of self.console.print()

    def flush(self):
        """Flush method required for stdout override."""
        pass

if __name__ == "__main__":
    cli = TerminalCLI()
    cli.run()
