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

from unittest import mock

from esi.v1 import _proxy
from esi.v1 import event
from esi.v1 import lease
from esi.v1 import node
from esi.v1 import offer

from openstack.tests.unit import test_proxy_base

_MOCK_METHOD = 'esi.v1._proxy.Proxy._get_with_fields'


class TestESIProxy(test_proxy_base.TestProxyBase):
    def setUp(self):
        super(TestESIProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)


class TestOffer(TestESIProxy):
    @mock.patch.object(offer.Offer, 'list')
    def test_offers_detailed(self, mock_list):
        result = self.proxy.offers(details=True, query=1)
        self.assertIs(result, mock_list.return_value)
        mock_list.assert_called_once_with(self.proxy, details=True, query=1)

    @mock.patch.object(offer.Offer, 'list')
    def test_offers_not_detailed(self, mock_list):
        result = self.proxy.offers(query=1)
        self.assertIs(result, mock_list.return_value)
        mock_list.assert_called_once_with(self.proxy, details=False, query=1)

    def test_create_offer(self):
        self.verify_create(self.proxy.create_offer, offer.Offer)

    def test_get_offer(self):
        self.verify_get(
            self.proxy.get_offer,
            offer.Offer,
            mock_method=_MOCK_METHOD,
            expected_kwargs={'fields': None},
        )

    def test_claim_offer(self):
        self.verify_update(self.proxy.claim_offer, offer.Offer)

    def test_delete_offer(self):
        self.verify_delete(self.proxy.delete_offer, offer.Offer, False)

    def test_delete_offer_ignore(self):
        self.verify_delete(self.proxy.delete_offer, offer.Offer, True)


class TestLease(TestESIProxy):
    @mock.patch.object(lease.Lease, 'list')
    def test_leases_detailed(self, mock_list):
        result = self.proxy.leases(details=True, query=1)
        self.assertIs(result, mock_list.return_value)
        mock_list.assert_called_once_with(self.proxy, details=True, query=1)

    @mock.patch.object(lease.Lease, 'list')
    def test_leases_not_detailed(self, mock_list):
        result = self.proxy.leases(query=1)
        self.assertIs(result, mock_list.return_value)
        mock_list.assert_called_once_with(self.proxy, details=False, query=1)

    def test_create_lease(self):
        self.verify_create(self.proxy.create_lease, lease.Lease)

    def test_get_lease(self):
        self.verify_get(
            self.proxy.get_lease,
            lease.Lease,
            mock_method=_MOCK_METHOD,
            expected_kwargs={'fields': None},
        )

    def test_delete_lease(self):
        self.verify_delete(self.proxy.delete_lease, lease.Lease, False)

    def test_delete_lease_ignore(self):
        self.verify_delete(self.proxy.delete_lease, lease.Lease, True)


class TestNode(TestESIProxy):
    @mock.patch.object(node.Node, 'list')
    def test_nodes_detailed(self, mock_list):
        result = self.proxy.nodes(details=True)
        self.assertIs(result, mock_list.return_value)
        mock_list.assert_called_once_with(self.proxy, details=True)

    @mock.patch.object(node.Node, 'list')
    def test_nodes_not_detailed(self, mock_list):
        result = self.proxy.nodes()
        self.assertIs(result, mock_list.return_value)
        mock_list.assert_called_once_with(self.proxy, details=False)


class TestEvent(TestESIProxy):
    @mock.patch.object(event.Event, 'list')
    def test_events_detailed(self, mock_list):
        result = self.proxy.events(details=True, query=1)
        self.assertIs(result, mock_list.return_value)
        mock_list.assert_called_once_with(self.proxy, details=True, query=1)

    @mock.patch.object(event.Event, 'list')
    def test_events_not_detailed(self, mock_list):
        result = self.proxy.events(query=1)
        self.assertIs(result, mock_list.return_value)
        mock_list.assert_called_once_with(self.proxy, details=False, query=1)
