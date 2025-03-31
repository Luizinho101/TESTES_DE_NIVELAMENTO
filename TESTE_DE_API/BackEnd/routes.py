from flask import Blueprint, request, jsonify
from database import get_db_connection

search_bp = Blueprint('search', __name__)


@search_bp.route('/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('q')

    if not query:
        return jsonify({'error': 'Query parameter "q" is required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM registro_ans 
        WHERE razao_social ILIKE %s OR nome_fantasia ILIKE %s;
    """, ('%' + query + '%', '%' + query + '%'))

    operadoras = cur.fetchall()
    cur.close()
    conn.close()

    if not operadoras:
        return jsonify({'message': 'No results found'}), 404

    result = [{'id': op[0], 'razao_social': op[1], 'nome_fantasia': op[2]}
              for op in operadoras]

    return jsonify(result)
