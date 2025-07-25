import subprocess
import sys
import time

# 🚀 Auto-installation des modules manquants
modules = ["typer", "rich", "pyfiglet", "pikepdf"]
for module in modules:
    try:
        __import__(module)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# ✅ Import après installation
import typer
import pikepdf
from pyfiglet import Figlet
import os

# 🎨 ASCII Art + Signature perso
ascii_art = Figlet(font='slant')
print(ascii_art.renderText('INIYA'))

print("Made by  : Iniya Merci")
print("Github   : https://github.com/Perians")
print("WhatsApp : +25766024133\n")

# ⚙️ Typer CLI
app = typer.Typer(help="🔐 INIYA PDF Cracker - Brute force d'un PDF protégé")

@app.command()
def crack(pdf: str = typer.Option(..., "--pdf", "-f", help="Chemin du fichier PDF protégé"),
          wordlist: str = typer.Option(..., "--wordlist", "-w", help="Chemin de la wordlist"),
          output: str = typer.Option(None, "--output", "-o", help="Nom du PDF déverrouillé (optionnel)")):
    """
    🔓 Brute force d'un fichier PDF protégé.
    """
    if not os.path.exists(pdf):
        typer.secho("❌ Fichier PDF introuvable.", fg=typer.colors.RED)
        raise typer.Exit()

    if not os.path.exists(wordlist):
        typer.secho("❌ Wordlist introuvable.", fg=typer.colors.RED)
        raise typer.Exit()

    output = output or f"deverrouille_{os.path.basename(pdf)}"

    with open(wordlist, "r") as f:
        passwords = f.readlines()

    typer.secho(f"📂 Cible : {pdf}", fg=typer.colors.CYAN)
    typer.secho(f"📖 Wordlist : {wordlist}", fg=typer.colors.CYAN)
    typer.secho("🚀 Début du brute force...\n", fg=typer.colors.YELLOW)

    for password in passwords:
        password = password.strip()
        sys.stdout.write(f"\r🔐 Test du mot de passe : {password} ")
        sys.stdout.flush()
        time.sleep(0.01)

        try:
            with pikepdf.open(pdf, password=password) as pdf_file:
                pdf_file.save(output)
                print()  # Saut de ligne après succès
                typer.secho(f"\n✅ Mot de passe trouvé : {password}", fg=typer.colors.GREEN, bold=True)
                typer.secho(f"📁 PDF déverrouillé enregistré : {output}", fg=typer.colors.BLUE)
                return
        except pikepdf.PasswordError:
            continue
        except Exception as e:
            typer.secho(f"\n⚠️ Erreur : {str(e)}", fg=typer.colors.RED)

    print()
    typer.secho("\n🚫 Aucun mot de passe correct dans la wordlist.", fg=typer.colors.BRIGHT_RED, bold=True)

if __name__ == "__main__":
    app()
