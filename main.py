import hub

hub.CONSTANTS.initialize_databases()

print(f"{hub.Fore.BLUE}\n", hub.CONSTANTS.DATABASE.load("/game/0/name"), f"{hub.Fore.RESET}")

hub.delay_print(
    hub.CONSTANTS.DATABASE.load("/game/0/parts/intro")
)


hub.time.sleep(50)