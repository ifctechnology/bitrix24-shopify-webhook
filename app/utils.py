import requests

def get_cari_code_by_email(email):
    """Fetch the Cari Code from Bitrix24 by email."""
    url = "https://[your_bitrix24_domain]/rest/[user_id]/[auth_key]/crm.contact.list"
    params = {"filter[EMAIL]": email}
    response = requests.get(url, params=params)
    if response.status_code == 200 and response.json()['result']:
        return response.json()['result'][0]['UF_CRM_CARI_CODE']
    return None

def update_customer_metafield(customer_id, cari_code):
    """Update the Shopify customer metafield."""
    url = f"https://[your_shopify_store].myshopify.com/admin/api/2023-10/customers/{customer_id}/metafields.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": "[your_shopify_access_token]"
    }
    payload = {
        "metafield": {
            "namespace": "custom",
            "key": "cari_code",
            "value": cari_code,
            "type": "string"
        }
    }
    response = requests.put(url, json=payload, headers=headers)
    return response.status_code == 200
