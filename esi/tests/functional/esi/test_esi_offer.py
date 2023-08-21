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

import datetime

from esi.tests.functional.esi import base
from openstack import exceptions

start = datetime.datetime(2016, 7, 16, 19, 20, 30)


class TestESIOffer(base.BaseESITest):
    def setUp(self):
        super(TestESIOffer, self).setUp()

    def test_offer_create(self):
        offer = self.create_offer('1718', 'dummy_node')

        self.assertNotEqual(offer, {})

        self.conn.esi.delete_offer(offer, ignore_missing=False)
        self.assertRaises(
            exceptions.ResourceNotFound, self.conn.esi.get_offer, offer.id
        )

    def test_offer_list(self):
        offer = self.create_offer('1718', 'dummy_node')
        offers = self.conn.esi.offers(resource_id='1718')
        self.assertEqual([o.offer_id for o in offers], [offer.offer_id])
