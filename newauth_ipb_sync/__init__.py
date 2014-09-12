import json
from flask import current_app, render_template_string, url_for, request
from flask.ext.sqlalchemy import models_committed
from newauth.models import db, User, redis, Group, AuthContact


class IPBSync(object):
    """IPB Sync module for NewAuth"""

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        self.app.logger.debug("IPB Sync is enabled.")

        # Registering events
        models_committed.connect_via(app)(self.handle_commit)

    def handle_commit(self, app, changes):
        # Disable signals when sending a ping
        if request and request.endpoint == 'PingsView:new' and request.method == 'POST':
            return
        for model, change in changes:
            if isinstance(model, User):
                if change == 'update':
                    # TODO
                    pass
            if isinstance(model, Group):
                self.update_groups(model)
            if isinstance(model, AuthContact):
                self.update_contacts(model)

    def update_contacts(self, model):
        session = db.create_scoped_session()
        redis.set('newauth_ipb_contacts', json.dumps([
            contact.name for contact in session.query(AuthContact).all()
        ]))

    def update_groups(self, model):
        session = db.create_scoped_session()
        redis.set('newauth_ipb_groups', json.dumps([
            group.name for group in session.query(Group).all()
        ]))
