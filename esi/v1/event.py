#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from openstack import resource


class Event(resource.Resource):
    resources_key = 'events'
    base_path = '/events'

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True
    commit_method = 'PATCH'
    commit_jsonpatch = True

    # client-side query parameter
    _query_mapping = resource.QueryParameters(
        'ID',
        'event_type',
        'event_time',
        'resource_type',
        'resource_uuid'
    )

    #: The transaction date and time.
    timestamp = resource.Header("x-timestamp")
    #: The value of the resource. Also available in headers.
    uuid = resource.Body("id", alias="x-resource-value")
    event_type = resource.Body("event_type")
    event_time = resource.Body("event_time")
    object_type = resource.Body("object_type")
    object_uuid = resource.Body("object_uuid")
    resource_type = resource.Body("resource_type")
    resource_uuid = resource.Body("resource_uuid")
    lease_id = resource.Body("lease_id")
    owner_id = resource.Body("owner_id")


EventDetail = Event
