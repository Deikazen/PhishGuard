from flask import request, jsonify
from app.services.feedback_service import save_feedback_to_sheets

def feedback():
    """Controller untuk endpoint /api/feedback"""
    try:
        # 1. Ambil data dari request frontend
        data = request.get_json()
        pesan = data.get('pesan')
        
        # 2. Validasi input
        if not pesan or str(pesan).strip() == "":
            return jsonify({"error": "Pesan tidak boleh kosong"}), 400

        # 3. Lempar data ke Service untuk disimpan
        save_feedback_to_sheets(pesan)

        # 4. Beri respon sukses ke frontend
        return jsonify({"message": "Feedback berhasil dikirim!"}), 200

    except Exception as e:
        # Jika terjadi error di service atau controller, tangkap di sini
        print(f"Feedback Controller Error: {e}")
        return jsonify({"error": "Gagal mengirim feedback. Silakan coba lagi nanti."}), 500