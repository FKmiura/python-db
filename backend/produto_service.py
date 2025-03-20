import mysql.connector


def buscar(id):
  cnx = mysql.connector.connect(
      host="db",
      port=3306,
      user="root",
      password="root",
      database="produtodb")

  cur = cnx.cursor(dictionary=True)

  cur.execute("SELECT * FROM produto WHERE id = " + id)
  myresult = cur.fetchone()

  cnx.close()
  return myresult


def listar():
  cnx = mysql.connector.connect(
      host="db",
      port=3306,
      user="root",
      password="root",
      database="produtodb")

  cur = cnx.cursor(dictionary=True)

  cur.execute("SELECT * FROM produto")
  myresult = cur.fetchall()

  cnx.close()
  return myresult


def adicionar(data):
  pass


def editar(data):
  pass


def excluir(id):
  cnx = mysql.connector.connect(
      host="db",
      port=3306,
      user="root",
      password="root",
      database="produtodb")

  cur = cnx.cursor(dictionary=True)

  cur.execute("DELETE FROM produto WHERE id = " + id)
  cnx.commit()

  rows = cur.rowcount

  cnx.close()
  return str(rows) + " record(s) deleted"
