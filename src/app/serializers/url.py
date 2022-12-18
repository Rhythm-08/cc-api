from typing import Any
from app.database.models.url import Url


def serialize_url(url: Url, include_stats=False) -> dict[str, Any]:
    serialized_url = {
        "id": url.id,
        "redirect_url": url.redirect,
        "hash": url.hash,
        "expire_at_timestamp": url.expiration_date.timestamp(),
    }

    if include_stats:
        serialized_url["views"] = url.views

    return {"url": serialized_url}
