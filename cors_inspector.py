import argparse,json
from pathlib import Path
def inspect(headers):
 h={k.strip().lower():v.strip() for k,v in (line.split(":",1) for line in headers.splitlines() if ":" in line)}
 origin=h.get("access-control-allow-origin","")
 credentials=h.get("access-control-allow-credentials","").lower()=="true"
 notes=[]
 if origin=="*":notes.append("Wildcard origin allows any requesting origin for non-credentialed requests.")
 if origin=="*" and credentials:notes.append("Wildcard origin with credentials is invalid in browsers and should be reviewed.")
 if credentials and origin and origin!="*":notes.append("Credentialed CORS: verify the origin is strictly allowlisted.")
 return {"allow_origin":origin or None,"allow_credentials":credentials,"notes":notes}
def main():
 p=argparse.ArgumentParser();p.add_argument("file");x=p.parse_args();print(json.dumps(inspect(Path(x.file).read_text(encoding="utf-8")),indent=2))
if __name__=="__main__":main()
