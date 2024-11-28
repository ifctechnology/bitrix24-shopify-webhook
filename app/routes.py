from flask import Blueprint, request, jsonify
from .utils import get_cari_code_by_email, update_customer_metafield

webhook = Blueprint('webhook', __name__)

@webhook.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    email = data.get('email')
    customer_id = data.get('id')

    if not email or not customer_id:
        return jsonify({"error": "Invalid data"}), 400

    # Get IFC Cari Code from Bitrix24
    cari_code = get_cari_code_by_email(email)
    if not cari_code:
        return jsonify({"message": "No matching Cari Code found"}), 404

    # Update Shopify metafield
    success = update_customer_metafield(customer_id, cari_code)
    if success:
        return jsonify({"message": "Metafield updated successfully"}), 200

    return jsonify({"message": "Failed to update metafield"}), 500
