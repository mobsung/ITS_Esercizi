from volo import Volo
from voloCommerciale import VoloCommerciale
from voloCharter import VoloCharter
from compagnia_aerea import CompagniaAerea



if __name__ == '__main__':

    with open("report.txt", "w", encoding="utf-8") as file:

        volo_commerciale1 = VoloCommerciale("COM123", 100)

        file.write("Posti disponibili sul volo commerciale COM123:\n")
        file.write(str(volo_commerciale1.posti_disponibili()) + "\n")

        volo_commerciale1.prenota_posto(70, "ecconomica")
        file.write(str(volo_commerciale1.posti_disponibili()) + "\n")

        volo_commerciale1.prenota_posto(20, "business")
        file.write(str(volo_commerciale1.posti_disponibili()) + "\n")

        if volo_commerciale1.posti_disponibili()["prima"] < 70:
            file.write(f"Non è possibile riservare 70 posti in prima classe. Numero posti disponibili: {volo_commerciale1.posti_disponibili()['prima']}\n")
        file.write(str(volo_commerciale1.posti_disponibili()) + "\n")

        volo_commerciale1.prenota_posto(10, "prima")
        file.write(str(volo_commerciale1.posti_disponibili()) + "\n")

        volo_commerciale1.prenota_posto(1, "ecconomica")  # Volo completo

        file.write("\n")

        volo_charter1 = VoloCharter("CHA456", 200, 20000.0)
        file.write(f"Posti disponibili sul volo charter {volo_charter1.codiceVolo()}: {volo_charter1.posti_disponibili()}\n")
        volo_charter1.prenota_posto(200)
        volo_charter1.prenota_posto(1)

        file.write("\n")

        volo_commerciale2 = VoloCommerciale("COM456", 100)
        volo_commerciale2.prenota_posto(100, "ecconomica")

        file.write("\n")

        compagnia = CompagniaAerea("ITA", 60.9)
        compagnia.aggiungi_volo(volo_commerciale1)
        compagnia.aggiungi_volo(volo_commerciale2)

        file.write("Ecco la flotta della compagnia aerea ITA:\n")
        file.write(str(compagnia.mostra_flotta()))

        file.write(f"\nDalla vendita dei biglietti aerei, la compagnia aerea ITA ha guadagnato {compagnia.guadagno()} euro\n")

