from sqlalchemy import create_engine, text

db_string = "mysql+pymysql://3iac7jtujrmgho3npd75:pscale_pw_gtBbLIRhBSLOin01Dl7UYJ646TmeelnRjkoZDR9sDuo@gcp.connect.psdb.cloud/diegocarrers?charset=utf8mb4"

engine = create_engine(db_string,
                      connect_args={
                        "ssl":{"ssl_ca":""}})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []

  for row in result.all():
    result_dicts.append(dict(row._asdict()))

  print(result_dicts)

  '''
    print(type(result))
    result_all = result.all()
    #result_li = result.all()
    print("\n")
    print(type(result_all))
    first = result_all[0]
    print(type(first))
    first_dic = dict(result_all[0]._asdict())
    print("first_dic type:", type(first_dic))
    print(first_dic)
    '''