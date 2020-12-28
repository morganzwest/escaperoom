import hub

hub.CONSTANTS.initialize_databases()

print(hub.CONSTANTS.DATABASE.load())