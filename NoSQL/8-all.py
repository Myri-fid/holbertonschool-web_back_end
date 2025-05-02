#!/usr/bin/env python3
"""List all documznts in a collection"""


def list_all(mongo_collection):
    """List all documznts in a collection"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
