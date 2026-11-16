"""Add and remove favorites (Robert)."""

from store import exists, insert, delete


def add_favorite(app_id, username, item_id):
    """Save a favorite, or report that it is already saved."""
    # Check this user's favorites within the specified application.
    if exists(app_id, username, item_id):
        return "duplicate"

    insert(app_id, username, item_id)
    return "added"


def remove_favorite(app_id, username, item_id):
    """Remove a favorite, or report that it was not found."""
    if not exists(app_id, username, item_id):
        return "not_found"

    # The storage function deletes only this app/user/item combination.
    delete(app_id, username, item_id)
    return "removed"
