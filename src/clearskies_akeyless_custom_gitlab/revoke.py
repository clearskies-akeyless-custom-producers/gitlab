from typing import Any

import clearskies
import requests

from clearskies_akeyless_custom_gitlab.common import verify_api_host
from clearskies_akeyless_custom_gitlab.errors import GitlabError


def revoke(
    id_to_delete: str | int,
    group_id: str | int,
    personal_access_token: str,
    requests: requests.Session,
    api_url: str = "https://gitlab.com/api/v4",
) -> None:
    """
    Revoke a GitLab group access token for the specified group and token ID.

    Args:
        id_to_delete (str | int): The ID of the group access token to revoke. May include group ID as a suffix.
        group_id (str | int): The GitLab group ID associated with the token.
        personal_access_token (str): Personal access token with permissions to revoke group access tokens.
        requests (requests.Session): HTTP session for making API calls.
        api_url (str, optional): Base URL for the GitLab API. Default is "https://gitlab.com/api/v4".

    Returns:
        None

    Raises:
        GitlabError: If the GitLab API returns an error or the revocation fails.
    """
    verify_api_host(api_url, personal_access_token, requests)

    if "_group_id_" in str(id_to_delete):
        [id_to_delete, group_id] = str(id_to_delete).split("_group_id_")

    response = requests.delete(
        f"{api_url}/groups/{group_id}/access_tokens/{id_to_delete}",
        headers={"PRIVATE-TOKEN": personal_access_token},
    )
    if not response.ok:
        raise GitlabError(response.text, api_url)
