from db import DataBase
import email_manager
import core


db = DataBase()

# Get clients from DB
clients = db.getClients()

# For each client get filters
for client in clients:
    filters = db.getFilters(client.get("id"))

    mail = email_manager.newMail(client)

    # For each filter send query
    for filter in filters:
        resume = core.getResume(filter)

        # Create email structure
        mail.add(resume)

    # Send email
    email_manager.send(mail)
