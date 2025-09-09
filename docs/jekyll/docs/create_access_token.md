---
title: Creating a GitLab Personal Access Token for Dynamic Credentials
layout: default
---

This guide explains how to generate temporary GitLab credentials using group access tokens, and why a personal access token is required.

## Why Use a Personal Access Token?

- Only a **personal access token** allows you to create and manage group access tokens via the GitLab API.
- You must be the **owner of the group** to generate group access tokens for that group.
- The personal access token must have the `api` and `self_rotate` scope to enable these operations.

## Important Limitations

- When you rotate a personal access token, GitLab automatically sets its lifetime to one week. Your rotation period must be **less than 7 days** or your credentials will expire and break the integration.

## Steps to Create a Personal Access Token

1. Go to your GitLab profile settings and create a new personal access token.
2. Select the **"api" scope** when creating the token.
3. Make sure you are the owner of the group for which you want to generate group access tokens.

## How to Find Your Personal Access Token ID

The GitLab UI does not display the token ID. To retrieve it, use the following API call:

```bash
curl -H "PRIVATE-TOKEN: <YOUR_PERSONAL_ACCESS_TOKEN>" 'https://gitlab.com/api/v4/personal_access_tokens?state=active' | jq
```

Find the token you just created in the output and note its `id`. You will need this ID for API operations and credential rotation.

## Summary

- Use a personal access token with the `api` and `self_rotate` scope.
- Only group owners can create group access tokens.
- Set your rotation period to less than 7 days.
- Retrieve your token ID via the API for use in automation.
