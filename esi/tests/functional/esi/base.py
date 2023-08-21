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

from openstack.tests.functional import base


class BaseESITest(base.BaseFunctionalTest):
    min_microversion = None

    def setUp(self):
        super(BaseESITest, self).setUp()
        self.require_service(
            'esi', min_microversion=self.min_microversion
        )

    def create_offer(self, node_id=None, resource_type=None, **kwargs):
        offer = self.conn.esi.create_offer(resource_id=node_id,
                                           resource_type=resource_type,
                                           **kwargs)
        self.addCleanup(
            lambda: self.conn.esi.delete_offer(
                offer.offer_id, ignore_missing=True
            )
        )
        return offer
