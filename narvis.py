import os
from skills.projects import create_project
from skills.notes import add_note_to_project, list_projects
from skills.inbox import list_inbox_items, read_inbox_item, move_inbox_to_project, INBOX_DIR
from skills.decisions import add_decision_to_project

def show_help():
    print("\nBeschikbare commando's:")
    print(" inbox       -> voeg iets toe aan de inbox")
    print(" project     -> maak een nieuw project")
    print(" notes       -> voeg een notitie toe aan een project")
    print(" decision    -> voeg een beslissing toe aan een project")
    print(" process     -> verwerk inbox-item naar project")
    print(" help        -> toon deze lijst")
    print(" exit        -> stop Narvis\n")

def run_narvis():
    print("Narvis is actief.")
    show_help()

    while True:
        command = input("> ").strip().lower()

        if not command:
            continue

        if command == "exit":
            print("Narvis sluit af.")
            break

        elif command == "help":
            show_help()

        elif command == "inbox":
            text = input("Wat wil je toevoegen aan de inbox?\n> ").strip()
            if text:
                from skills.inbox import add_to_inbox  # alleen voor toevoegen aan inbox
                filepath = add_to_inbox(text)
                print(f"Inbox-item opgeslagen: {filepath}\n")


        elif command == "project":
            name = input("Projectnaam: ").strip()
            description = input("Beschrijving (optioneel): ").strip()
            goal = input("Doel (optioneel): ").strip()

            print("\nTemplates beschikbaar:")
            print("1. Notities-project (notes.md)")
            print("2. Data-project (project.xlsx)")
            print("3. Full-project (notes.md + project.docx)")
            print("4. Script-project (script.py)")
            print("5. Maatwerk (je kiest zelf)")

            template_choice = input("Kies template nummer (standaard 3): ").strip() or "3"

            template_map = {
                "1": ["notes.md"],
                "2": ["project.xlsx"],
                "3": ["notes.md", "project.docx"],
                "4": ["script.py"],
                "5": None  # zelf kiezen
            }

            files_to_create = template_map.get(template_choice, ["notes.md", "project.docx"])

            # Als maatwerk
            if template_choice == "5":
                custom_files = input("Welke bestanden wil je aanmaken? (scheid met komma, bijv: notes.md, script.py): ").strip()
                files_to_create = [f.strip() for f in custom_files.split(",") if f.strip()]

            try:

                project_id = create_project(name, description, goal, files_to_create)
                print(f"Project aangemaakt: {project_id}\n")
            except FileExistsError as e:
                print(str(e) + "\n")

        elif command == "notes":
            projects = list_projects()

            if not projects:
                print("Geen projecten gevonden.\n")
                continue

            print("Beschikbare projecten:")
            for p in projects:
                print(f"- {p}")

            project_id = input("Kies project (id): ").strip()

            if project_id not in projects:
                print("Ongeldig project.\n")
                continue

            text = input("Notitie:\n> ").strip()

            if text:
                add_note_to_project(project_id, text)
                print("Notitie toegevoegd. \n")


        elif command == "decision":
            projects = list_projects()

            if not projects:
                print("Geen projecten gevonden.\n")
                continue

            print("Beschikbare projecten:")
            for p in projects:
                print(f"- {p}")

            project_id = input("Kies project (id): ").strip()

            if project_id not in projects:
                print("Ongeldig project.\n")
                continue

            decision = input("Wat is de beslissing?\n> ").strip()
            reason = input("Waarom deze beslissing?\n> ").strip()
            alternatives = input("Alternatieven (optioneel):\n> ").strip()
            impact = input("Gevolgen / impact (optioneel):\n> ").strip()

            add_decision_to_project(
                project_id,
                decision,
                reason,
                alternatives,
                impact
            )

            print("Beslissing toegevoegd aan beslissingen-log.\n")


        elif command == "process":
            inbox_items = list_inbox_items()

            if not inbox_items:
                print("Inbox is leeg.\n")
                continue

            print("Inbox-items:")
            for i, item in enumerate(inbox_items, start=1):
                print(f"{i}. {item}")

            try:
                choice = int(input("Kies inbox-item nummer: "))
                filename = inbox_items[choice - 1]
            except (ValueError, IndexError):
                print("Ongeldige keuze.\n")
                continue

            content = read_inbox_item(filename)
            print("\nInhoud:")
            print(content)
            print("\nBeschikbare projecten:")

            projects = list_projects()
            for p in projects:
                print(f"- {p}")

            project_id = input("Verplaatsen naar project (id): ").strip()

            if project_id not in projects:
                print("Ongeldig project.\n")
                continue

            inbox_file = os.path.join(INBOX_DIR, str(filename))

            # Verplaats naar projectnotities (verwijdert automatisch uit inbox)
            new_path = move_inbox_to_project(inbox_file, project_id)

            print(f"Inbox-item verwerkt en toegevoegd aan project: {new_path}\n")

        else:
            print("Onbekend commando. Typ 'help' voor opties.\n")

if __name__ == "__main__":
    run_narvis()
