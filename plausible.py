#!/usr/bin/python

import requests
import json


class PlausibleAPI(object):
    CREATE_SITE_URL = "/api/v1/sites"
    RETRIEVE_SITE_URL = "/api/v1/sites/{domain}"
    UPDATE_SITE_URL = "/api/v1/sites/{domain}"
    DELETE_SITE_URL = "/api/v1/sites/{domain}"

    CREATE_SITE_SHARED_LINK_URL = "/api/v1/sites/shared-links"

    CREATE_SITE_GOAL_URL = "/api/v1/sites/goals"
    DELETE_SITE_GOAL_URL = "/api/v1/sites/goals/{goal_id}"

    SEND_EVENT_URL = "/api/event"

    REALTIME_VISITOR_URL = "/api/v1/stats/realtime/visitors?site_id={domain}"

    def __init__(self, host, token):
        self.host = host

        self.headers = {
            'Authorization': 'Bearer '+token, 
            'Content-Type': 'application/json'
        }

        self.result = dict(
            message=''
        )

    def build_url(self, url):
        required_url = self.host + url

        return required_url

    def get_url(self, task):
        if task == 'create-site':
            return self.build_url(self.CREATE_SITE_URL)
        elif task == 'retrieve-site':
            return self.build_url(self.RETRIEVE_SITE_URL.format(
                        domain=self.domain
                    ))
        elif task == 'update-site':
            return self.build_url(self.UPDATE_SITE_URL.format(
                        domain=self.domain
                    ))
        elif task == 'delete-site':
            return self.build_url(self.DELETE_SITE_URL.format(
                        domain=self.domain
                    ))
        elif task == 'create-site-goal':
            return self.build_url(self.CREATE_SITE_GOAL_URL)
        elif task == 'delete-site-goal':
            return self.build_url(self.DELETE_SITE_GOAL_URL.format(
                        goal_id=self.goal_id
                    ))
        elif task == 'create-site-shared-link':
            return self.build_url(self.CREATE_SITE_SHARED_LINK_URL)
        elif task == 'send-event':
            return self.build_url(self.SEND_EVENT_URL)
        elif task == 'realtime-visitors':
            return self.build_url(self.REALTIME_VISITOR_URL.format(
                        domain=self.domain
                    ))

    def create_site(self, domain, time_zone):
        result = self.result

        payload = {
            'domain': domain,
            'timezone': time_zone
        }

        create_site_url = self.get_url('create-site')

        create_requests = requests.post(create_site_url, data=json.dumps(payload), headers=self.headers)

        result['url'] = create_site_url
        result['payload'] = payload
        result['status_code'] = create_requests.status_code
        result['response'] = create_requests.json()
        
        if create_requests.status_code == 200:
            result['message'] = "Site has been created"
        else:
            result['message'] = "Failed to create site"
        
        return result

    def retrieve_site(self, domain):
        self.domain = domain
        retrieve_site_url = self.get_url('retrieve-site')

        result = self.result
        retrieve_requests = requests.get(retrieve_site_url, headers=self.headers)

        result['url'] = retrieve_site_url
        result['status_code'] = retrieve_requests.status_code
        result['response'] = retrieve_requests.json()

        if retrieve_requests.status_code == 200:
            result['message'] = "Site is available"
        else:
            result['message'] = "Site not found"

        return result

    def update_site(self, domain, new_domain):
        self.domain = domain
        update_site_url = self.get_url('update-site')

        payload = {
            'domain': new_domain
        }

        result = self.result
        update_requests = requests.put(update_site_url, data=json.dumps(payload), headers=self.headers)

        result['url'] = update_site_url
        result['status_code'] = update_requests.status_code
        result['response'] = update_requests.json()

        if update_requests.status_code == 200:
            result['changed'] = True
            result['message'] = "Site has been updated"
        else:
            result['changed'] = False
            result['message'] = "Site can't be updated"
        
        return result

    def delete_site(self, domain):
        self.domain = domain
        delete_site_url = self.get_url('delete-site')

        result = self.result
        delete_requests = requests.delete(delete_site_url, headers=self.headers)

        result['message'] = "Site has been deleted"
        result['url'] = delete_site_url
        result['status_code'] = delete_requests.status_code
        result['response'] = delete_requests.json()

        if delete_requests.status_code == 200:
            result['changed'] = True
            result['message'] = "Site has been deleted"
        else:
            result['changed'] = False
            result['message'] = "Site can't be deleted"

        return result

    def create_site_goal(self, domain, goal_type, event_name="", page_path=""):
        result = self.result

        if goal_type == "event":
            payload = {
                'site_id': domain,
                'goal_type': goal_type,
                'event_name': event_name,
            }
        elif goal_type == "page":
            payload = {
                'site_id': domain,
                'goal_type': goal_type,
                'page_path': page_path
            }

        create_site_goal_url = self.get_url('create-site-goal')

        create_requests = requests.put(create_site_goal_url, data=json.dumps(payload), headers=self.headers)

        result['url'] = create_site_goal_url
        result['payload'] = payload
        result['status_code'] = create_requests.status_code
        result['response'] = create_requests.json()
        
        if create_requests.status_code == 200:
            result['message'] = "Site goal has been created"
        else:
            result['message'] = "Site goal couldn't be created"

        return result

    def delete_site_goal(self, goal_id, domain):
        self.goal_id = goal_id
        delete_site_goal_url = self.get_url('delete-site-goal')

        payload = {
            'site_id': domain,
        }

        result = self.result
        delete_requests = requests.delete(delete_site_goal_url, data=json.dumps(payload), headers=self.headers)

        result['url'] = delete_site_goal_url
        result['status_code'] = delete_requests.status_code

        if delete_requests.status_code == 200:
            result['changed'] = True
            result['message'] = "Site goal has been deleted"
        else:
            result['changed'] = False
            result['message'] = "Site goal can't be deleted"

        return result

    def create_site_shared_link(self, domain, name):
        result = self.result

        payload = {
            'site_id': domain,
            'name': name,
        }

        create_site_shared_link_url = self.get_url('create-site-shared-link')

        create_requests = requests.put(create_site_shared_link_url, data=json.dumps(payload), headers=self.headers)

        result['url'] = create_site_shared_link_url
        result['payload'] = payload
        result['status_code'] = create_requests.status_code
        result['response'] = create_requests.json()
        
        if create_requests.status_code == 200:
            result['message'] = "Site shared link has been created"
        else:
            result['message'] = "Site shared link couldn't be created"

        return result

    def send_event(self, user_agent, domain, name, url, x_forwarded_for="", props={}, currency="", amount=""):
        result = self.result

        self.headers['User-Agent'] = user_agent
        self.headers['X-Forwarded-For'] = x_forwarded_for

        payload = {
            'domain': domain,
            'name': name,
            'url': url,
            'props': props,
            'revenue': {
                "currency": currency,
                "amount": amount
            }
        }

        send_event_url = self.get_url('send-event')

        create_requests = requests.post(send_event_url, data=json.dumps(payload), headers=self.headers)

        result['url'] = send_event_url
        result['payload'] = payload
        result['status_code'] = create_requests.status_code
        
        if create_requests.status_code == 202:
            result['message'] = "Event has been sent"
            result['response'] = {}
        else:
            result['message'] = "Can't send event"
            result['response'] = create_requests.json()

        return result

    def get_realtime_visitors(self, domain):
        self.domain = domain
        realtime_visitors_url = self.get_url('realtime-visitors')

        result = self.result
        retrieve_requests = requests.get(realtime_visitors_url, headers=self.headers)

        result['url'] = realtime_visitors_url
        result['status_code'] = retrieve_requests.status_code
        result['response'] = retrieve_requests.json()

        if retrieve_requests.status_code == 200:
            result['message'] = "Realtime visitors successfully fetched"
        else:
            result['message'] = "Can't fetch realtime visitors"

        return result
