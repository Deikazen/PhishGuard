from app.services.feedback_service import init_csv, save_feedback_to_csv
from flask import request, jsonify

def feedback():
    init_csv()
    dataPesan = request.get_json()
    pesan = dataPesan.get("pesan")
   

    if not pesan:
        return jsonify({"message": "Pesan tidak boleh kosong"}), 400

    is_saved = save_feedback_to_csv(pesan)

    if is_saved:
        return jsonify({"status": "success", "message": "Feedback berhasil disimpan"}), 200
    else:
        return jsonify({"status": "error", "message": "Gagal menyimpan feedback"}), 500
