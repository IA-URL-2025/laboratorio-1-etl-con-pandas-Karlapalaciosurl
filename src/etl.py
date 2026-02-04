import pandas as pd

def run_etl():
    """
    Implementa el proceso ETL.
    No cambies el nombre de esta función.
    """
    # TODO: implementar
    #Extraer
    citas = pd.read_csv("data/citas_clinica.csv")

    citas["paciente"] = citas["paciente"].str.title()
    citas["especialidad"] = citas["especialidad"].str.upper()

    citas["fecha_cita"] = pd.to_datetime(citas["fecha_cita"], errors="coerce")
    citas = citas.dropna(subset=["fecha_cita"])

    citas = citas[citas["estado"] == "CONFIRMADA"]
    citas = citas[citas["costo"] > 0]

    citas["telefono"] = citas["telefono"].fillna("NO REGISTRA")

    citas.to_csv("data/output.csv", index=False)


if __name__ == "__main__":
    run_etl()
