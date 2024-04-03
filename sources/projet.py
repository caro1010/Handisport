import tkinter
from tkinter import*
import subprocess

#listes
sport=["Athletisme", "Badmintons_sourds", "Boccia", "Pétanque_sourds_haut_niveau", "Pétanque_sourds_loisir", "Bowlings_sourds", "Bowlings_sourds_loisir", "Cécifoot", "Cyclisme", "Danse", "Développé_couché_et_Musculation", "Escrime", "Foot_fauteuil_électrique", "Footballs_sourds", "Goalball", "Handball_Sourds", "Judo", "Natation", "Plongée_subaquatique", "Randonnée", "Rugby_fauteuil", "Sarbacane", "Showdown", "Ski_alpin", "Ski_Nordique", "Tennis", "Tennis_de_table", "Tir_a_l_arc", "Tir sportif", "Torball", "Voile"]
cardiovasculaire=["Sarbacane", "Tennis de table", "Tir Sportif", "Voile"]
auditif=["Athletisme", "Badmintons sourds", "Pétanque sourds haut niveau", "Pétanque sourds loisir", "Bowlings sourds", "Bowlings sourds loisir", "Cécifoot", "Danse", "Développé couché et musculation", "Escrime", "Footballs sourds", "Handball sourds", "Judo", "Natation", "Randonnée", "Sarbacane", "Ski nordique", "Tennis", "Tennis de table", "Tir sportif", "Voile"]
cérébral=["Athletisme", "Pétanque sourds loisir", "Bowlings sourds loisir", "Danse", "Développé couché et musculation", "Escrime", "Rugby fauteuil","Sarbacane", "Ski nordique", "Tir sportif"]
visuel=["Athletisme", "Pétanque sourds loisir", "Bowlings sourds loisir", "Danse", "Développé couché et musculation", "Goalball", "Judo", "Natation", "Plongée subaquatique", "Randonnée", "Sarbacane", "Showdown", "Ski alpin", "Ski nordique", "Tir a l'arc", "Tir sportif", "Torball", "Voile"]
physique_en_raison_de_la_taille=["Athletisme", "Pétanque sourds loisir", "Bowlings sourds loisir", "Danse", "Développé couché et musculation", "Plongée subaquatique", "Sarbacane", "Tennis de table", "Tir sportif", "Voile"]
physique_localisé_en_dessous_de_la_taille=["Athletisme","Pétanque sourds loisir", "Bowlings sourds loisir", "Cyclisme", "Danse", "Développé couché et musculation", "Escrime", "Foot fauteuil électrique", "Natation", "Plongée subaquatique", "Randonnée", "Rugby fauteuil", "Sarbacane", "Ski alpin", "Ski nordique", "Tennis", "Tennis de table", "Tir a l'arc", "Tir sportif", "Voile"]
physique_localisé_au_dessus_de_la_taille=["Boccia", "Pétanque sourds loisir", "Bowlings sourds loisir", "Cyclisme", "Danse", "Développé couché et musculation", "Escrime", "Foot fauteuil électrique", "Natation", "Plongée subaquatique", "Rugby fauteuil","Sarbacane", "Ski nordique", "Tir sportif", "Voile", "Tir a l'arc"]

def open2() :
    #coche
    c1 = choix1.get()
    c2 = choix2.get()
    c3 = choix3.get()
    c4 = choix4.get()
    c5 = choix5.get()
    c6 = choix6.get()
    c7 = choix7.get()

    #1 option
    if c1 == 1 and c2!=1 and c3!=1 and c4!=1 and c5!=1 and c6!=1 and c7!=1:
        print(cardiovasculaire)

    if c2 == 1 and c1!=1 and c3!=1 and c4!=1 and c5!=1 and c6!=1 and c7!=1:
        print(auditif)

    if c3 == 1 and c2!=1 and c1!=1 and c4!=1 and c5!=1 and c6!=1 and c7!=1:
        print(cérébral)

    if c4 == 1 and c2!=1 and c3!=1 and c1!=1 and c5!=1 and c6!=1 and c7!=1:
        print(visuel)

    if c5 == 1 and c2!=1 and c3!=1 and c4!=1 and c1!=1 and c6!=1 and c7!=1:
        print(physique_en_raison_de_la_taille)

    if c6 == 1 and c2!=1 and c3!=1 and c4!=1 and c5!=1 and c1!=1 and c7!=1:
        print(physique_localisé_en_dessous_de_la_taille)

    if c7 == 1 and c2!=1 and c3!=1 and c4!=1 and c5!=1 and c6!=1 and c1!=1:
        print(physique_localisé_au_dessus_de_la_taille)

    #2 options
    if c1==1 and c2==1 and c3!=1 and c4!=1 and c5!=1 and c6!=1 and c7!=1:
        c1_2=[]
        for i in cardiovasculaire :
            if i in auditif:
                c1_2.append(i)
        print(c1_2)

    if c1==1 and c3==1 and c2!=1 and c4!=1 and c5!=1 and c6!=1 and c7!=1:
        c1_3=[]
        for i in cardiovasculaire :
            if i in cérébral :
                c1_3.append(i)
        print(c1_3)

    if c1==1 and c4==1 and c2!=1 and c3!=1 and c5!=1 and c6!=1 and c7!=1:
        c1_4=[]
        for i in cardiovasculaire :
            if i in visuel :
                c1_4.append(i)
        print(c1_4)

    if c1==1 and c5==1 and c2!=1 and c4!=1 and c3!=1 and c6!=1 and c7!=1:
        c1_5=[]
        for i in cardiovasculaire :
            if i in physique_en_raison_de_la_taille :
                c1_5.append(i)
        print(c1_5)

    if c1==1 and c6==1 and c2!=1 and c4!=1 and c5!=1 and c3!=1 and c7!=1:
        c1_6=[]
        for i in cardiovasculaire :
            if i in physique_localisé_en_dessous_de_la_taille:
                c1_6.append(i)
        print(c1_6)

    if c1==1 and c7==1 and c2!=1 and c4!=1 and c5!=1 and c6!=1 and c3!=1:
        c1_7=[]
        for i in cardiovasculaire :
            if i in physique_localisé_au_dessus_de_la_taille :
                c1_7.append(i)
        print(c1_7)

    if c2==1 and c3==1 and c1!=1 and c4!=1 and c5!=1 and c6!=1 and c7!=1:
        c2_3=[]
        for i in auditif :
            if i in cérébral :
                c2_3.append(i)
        print(c2_3)

    if c2==1 and c4==1 and c1!=1 and c3!=1 and c5!=1 and c6!=1 and c7!=1:
        c2_4=[]
        for i in auditif :
            if i in visuel :
                c2_4.append(i)
        print(c2_4)

    if c2==1 and c5==1 and c1!=1 and c4!=1 and c3!=1 and c6!=1 and c7!=1:
        c2_5=[]
        for i in auditif :
            if i in physique_en_raison_de_la_taille :
                c2_5.append(i)
        print(c2_5)

    if c2==1 and c6==1 and c1!=1 and c4!=1 and c5!=1 and c3!=1 and c7!=1:
        c2_6=[]
        for i in auditif :
            if i in physique_localisé_en_dessous_de_la_taille :
                c2_6.append(i)
        print(c2_6)

    if c2==1 and c7==1 and c1!=1 and c4!=1 and c5!=1 and c6!=1 and c3!=1:
        c2_7=[]
        for i in auditif :
            if i in physique_localisé_au_dessus_de_la_taille :
                c2_7.append(i)
        print(c2_7)

    if c3==1 and c4==1 and c1!=1 and c2!=1 and c5!=1 and c6!=1 and c7!=1:
        c3_4=[]
        for i in cérébral :
            if i in visuel :
                c3_4.append(i)
        print(c3_4)

    if c3==1 and c5==1 and c1!=1 and c2!=1 and c4!=1 and c6!=1 and c7!=1:
        c3_5=[]
        for i in cérébral :
            if i in physique_en_raison_de_la_taille :
                c3_5.append(i)
        print(c3_5)

    if c3==1 and c6==1 and c1!=1 and c2!=1 and c5!=1 and c4!=1 and c7!=1:
        c3_6=[]
        for i in cérébral :
            if i in physique_localisé_en_dessous_de_la_taille :
                c3_6.append(i)
        print(c3_6)

    if c3==1 and c7==1 and c1!=1 and c2!=1 and c5!=1 and c6!=1 and c4!=1:
        c3_7=[]
        for i in cérébral :
            if i in physique_localisé_au_dessus_de_la_taille :
                c3_7.append(i)
        print(c3_7)

    if c4==1 and c5==1 and c1!=1 and c2!=1 and c3!=1 and c6!=1 and c7!=1:
        c4_5=[]
        for i in visuel :
            if i in physique_en_raison_de_la_taille :
                c4_5.append(i)
        print(c4_5)

    if c4==1 and c6==1 and c1!=1 and c2!=1 and c3!=1 and c5!=1 and c7!=1:
        c4_6=[]
        for i in visuel :
            if i in physique_localisé_en_dessous_de_la_taille :
                c4_6.append(i)
        print(c4_6)

    if c4==1 and c7==1 and c1!=1 and c2!=1 and c3!=1 and c6!=1 and c5!=1:
        c4_7=[]
        for i in visuel :
            if i in physique_localisé_au_dessus_de_la_taille :
                c4_7.append(i)
        print(c4_7)

    if c5==1 and c6==1 and c1!=1 and c2!=1 and c3!=1 and c4!=1 and c7!=1:
        c5_6=[]
        for i in physique_en_raison_de_la_taille :
            if i in physique_localisé_en_dessous_de_la_taille :
                c5_6.append(i)
        print(c5_6)

    if c5==1 and c7==1 and c1!=1 and c2!=1 and c3!=1 and c6!=1 and c4!=1:
        c5_7=[]
        for i in physique_en_raison_de_la_taille :
            if i in physique_localisé_au_dessus_de_la_taille :
                c5_7.append(i)
        print(c5_7)

    if c6==1 and c7==1 and c1!=1 and c2!=1 and c3!=1 and c4!=1 and c5!=1:
        c6_7=[]
        for i in physique_localisé_en_dessous_de_la_taille :
            if i in physique_localisé_au_dessus_de_la_taille :
                c6_7.append(i)
        print(c6_7)

    #3 options
    if c1==1 and c2==1 and c3==1 and c4!=1 and c5!=1 and c6!=1 and c7!=1:
        c1_2_3=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    c1_2_3.append(i)
        print(c1_2_3)

    if c1==1 and c2==1 and c4==1 and c3!=1 and c5!=1 and c6!=1 and c7!=1:
        c1_2_4=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in visuel :
                    c1_2_4.append(i)
        print(c1_2_4)

    if c1==1 and c2==1 and c5==1 and c3!=1 and c7!=1 and c6!=1 and c4!=1:
        c1_2_5=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in physique_en_raison_de_la_taille :
                    c1_2_5.append(i)
        print(c1_2_5)

    if c1==1 and c2==1 and c6==1 and c3!=1 and c5!=1 and c7!=1 and c4!=1:
        c1_2_6=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in physique_localisé_en_dessous_de_la_taille :
                    c1_2_6.append(i)
        print(c1_2_6)

    if c1==1 and c2==1 and c7==1 and c3!=1 and c5!=1 and c6!=1 and c4!=1:
        c1_2_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in physique_localisé_au_dessus_de_la_taille :
                    c1_2_7.append(i)
        print(c1_2_7)

    if c1==1 and c3==1 and c4==1 and c5!=1 and c6!=1 and c7!=1 and c2!=1:
        c1_3_4=[]
        for i in cardiovasculaire :
            if i in cérébral :
                if i in visuel :
                    c1_3_4.append(i)
        print(c1_3_4)

    if c1==1 and c3==1 and c5==1 and c4!=1 and c7!=1 and c6!=1 and c2!=1:
        c1_3_5=[]
        for i in cardiovasculaire :
            if i in cérébral :
                if i in physique_en_raison_de_la_taille :
                    c1_3_5.append(i)
        print(c1_3_5)

    if c1==1 and c3==1 and c6==1 and c4!=1 and c5!=1 and c7!=1 and c2!=1:
        c1_3_6=[]
        for i in cardiovasculaire :
            if i in cérébral :
                if i in physique_localisé_en_dessous_de_la_taille :
                    c1_3_6.append(i)
        print(c1_3_6)

    if c1==1 and c3==1 and c7==1 and c4!=1 and c5!=1 and c6!=1 and c2!=1:
        c1_3_7=[]
        for i in cardiovasculaire :
            if i in cérébral :
                if i in physique_localisé_au_dessus_de_la_taille :
                    c1_3_7.append(i)
        print(c1_3_7)

    if c1==1 and c4==1 and c5==1 and c3!=1 and c7!=1 and c6!=1 and c2!=1:
        c1_4_5=[]
        for i in cardiovasculaire :
            if i in visuel :
                if i in physique_en_raison_de_la_taille :
                    c1_4_5.append(i)
        print(c1_4_5)

    if c1==1 and c4==1 and c6==1 and c3!=1 and c5!=1 and c7!=1 and c2!=1:
        c1_4_6=[]
        for i in cardiovasculaire :
            if i in visuel :
                if i in physique_localisé_en_dessous_de_la_taille :
                    c1_4_6.append(i)
        print(c1_4_6)

    if c1==1 and c4==1 and c7==1 and c3!=1 and c5!=1 and c6!=1 and c2!=1:
        c1_4_7=[]
        for i in cardiovasculaire :
            if i in visuel :
                if i in physique_localisé_au_dessus_de_la_taille :
                    c1_4_7.append(i)
        print(c1_4_7)

    if c1==1 and c5==1 and c6==1 and c3!=1 and c4!=1 and c7!=1 and c2!=1:
        c1_5_6=[]
        for i in cardiovasculaire :
            if i in physique_en_raison_de_la_taille :
                if i in physique_localisé_en_dessous_de_la_taille :
                    c1_5_6.append(i)
        print(c1_5_6)

    if c1==1 and c5==1 and c7==1 and c3!=1 and c4!=1 and c6!=1 and c2!=1:
        c1_5_7=[]
        for i in cardiovasculaire :
            if i in physique_en_raison_de_la_taille :
                if i in physique_localisé_au_dessus_de_la_taille :
                    c1_5_7.append(i)
        print(c1_5_7)

    if c1==1 and c6==1 and c7==1 and c3!=1 and c5!=1 and c4!=1 and c2!=1:
        c1_6_7=[]
        for i in cardiovasculaire :
            if i in physique_localisé_en_dessous_de_la_taille :
                if i in physique_localisé_au_dessus_de_la_taille :
                    c1_6_7.append(i)
        print(c1_6_7)

    if c2==1 and c3==1 and c4==1 and c7!=1 and c5!=1 and c6!=1 and c1!=1:
        c2_3_4=[]
        for i in auditif :
            if i in cérébral :
                if i in visuel :
                    c2_3_4.append(i)
        print(c2_3_4)

    if c2==1 and c3==1 and c5==1 and c4!=1 and c7!=1 and c6!=1 and c1!=1:
        c2_3_5=[]
        for i in auditif :
            if i in cérébral :
                if i in physique_en_raison_de_la_taille :
                    c2_3_5.append(i)
        print(c2_3_5)

    if c2==1 and c3==1 and c6==1 and c4!=1 and c5!=1 and c7!=1 and c1!=1:
        c2_3_6=[]
        for i in auditif :
            if i in cérébral :
                if i in physique_localisé_en_dessous_de_la_taille :
                    c2_3_6.append(i)
        print(c2_3_6)

    if c2==1 and c3==1 and c7==1 and c4!=1 and c5!=1 and c6!=1 and c1!=1:
        c2_3_7=[]
        for i in auditif :
            if i in cérébral :
                if i in physique_localisé_au_dessus_de_la_taille :
                    c2_3_7.append(i)
        print(c2_3_7)

    if c2==1 and c4==1 and c5==1 and c3!=1 and c7!=1 and c6!=1 and c1!=1:
        c2_4_5=[]
        for i in auditif :
            if i in visuel :
                if i in physique_en_raison_de_la_taille :
                    c2_4_5.append(i)
        print(c2_4_5)

    if c2==1 and c4==1 and c6==1 and c3!=1 and c5!=1 and c7!=1 and c1!=1:
        c2_4_6=[]
        for i in auditif :
            if i in visuel :
                if i in physique_localisé_en_dessous_de_la_taille :
                    c2_4_6.append(i)
        print(c2_4_6)

    if c2==1 and c4==1 and c7==1 and c3!=1 and c5!=1 and c6!=1 and c1!=1:
        c2_4_7=[]
        for i in auditif :
            if i in visuel :
                if i in physique_localisé_au_dessus_de_la_taille :
                    c2_4_7.append(i)
        print(c2_4_7)


    #en cour...


    #4 Options
    if c1==1 and c2==1 and c3==1 and c4==1 and c5!=1 and c6!=1 and c7!=1:
        c1_2_3_4=[]
        for i in cardiovasculaire:
            if i in auditif:
                if i in cérébral:
                    if i in visuel:
                        c1_2_3_4.append(i)
        print(c1_2_3_4)

    if c1==1 and c2==1 and c3==1 and c4!=1 and c5==1 and c6!=1 and c7!=1:
        c1_2_3_5=[]
        for i in cardiovasculaire:
            if i in auditif:
                if i in cérébral:
                    if i in physique_en_raison_de_la_taille:
                        c1_2_3_5.append(i)
        print(c1_2_3_5)

    if c1==1 and c2==1 and c3!=1 and c4==1 and c5==1 and c6!=1 and c7!=1:
        c1_2_4_5=[]
        for i in cardiovasculaire:
            if i in auditif:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        c1_2_4_5.append(i)
        print(c1_2_4_5)

    if c1==1 and c2!=1 and c3==1 and c4==1 and c5==1 and c6!=1 and c7!=1:
        c1_3_4_5=[]
        for i in cardiovasculaire:
            if i in cérébral:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        c1_3_4_5.append(i)
        print(c1_3_4_5)

    if c1!=1 and c2==1 and c3==1 and c4==1 and c5==1 and c6!=1 and c7!=1:
        c2_3_4_5=[]
        for i in auditif:
            if i in cérébral:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        c2_3_4_5.append(i)
        print(c2_3_4_5)

    if c1!=1 and c2==1 and c3==1 and c4==1 and c5!=1 and c6==1 and c7!=1:
        c2_3_4_6=[]
        for i in auditif:
            if i in cérébral:
                if i in visuel:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        c2_3_4_6.append(i)
        print(c2_3_4_6)

    if c1!=1 and c2==1 and c3==1 and c4!=1 and c5==1 and c6==1 and c7!=1:
        c2_3_5_6=[]
        for i in auditif:
            if i in cérébral:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        c2_3_5_6.append(i)
        print(c2_3_5_6)

    if c1!=1 and c2==1 and c3!=1 and c4==1 and c5==1 and c6==1 and c7!=1:
        c2_4_5_6=[]
        for i in auditif:
            if i in visuel:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        c2_4_5_6.append(i)
        print(c2_4_5_6)


    if c1!=1 and c2!=1 and c3==1 and c4==1 and c5==1 and c6==1 and c7!=1:
        c3_4_5_6=[]
        for i in cérébral :
            if i in visuel:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        c3_4_5_6.append(i)
        print(c3_4_5_6)

    if c1!=1 and c2!=1 and c3==1 and c4==1 and c5==1 and c6!=1 and c7==1:
        c3_4_5_7=[]
        for i in cérébral :
            if i in visuel:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_au_dessus_de_la_taille:
                        c3_4_5_7.append(i)
        print(c3_4_5_7)

    if c1!=1 and c2!=1 and c3==1 and c4==1 and c5!=1 and c6==1 and c7==1:
        c3_4_6_7=[]
        for i in cérébral :
            if i in visuel:
                if i in physique_localisé_en_dessous_de_la_taille:
                    if i in physique_localisé_au_dessus_de_la_taille:
                        c3_4_6_7.append(i)
        print(c3_4_6_7)

    if c1!=1 and c2!=1 and c3==1 and c4!=1 and c5==1 and c6==1 and c7==1:
        c3_5_6_7=[]
        for i in cérébral :
            if i in physique_en_raison_de_la_taille:
                if i in physique_localisé_en_dessous_de_la_taille:
                    if i in physique_localisé_au_dessus_de_la_taille:
                        c3_5_6_7.append(i)
        print(c3_5_6_7)

    if c1!=1 and c2!=1 and c3!=1 and c4==1 and c5==1 and c6==1 and c7==1:
        c4_5_6_7=[]
        for i in visuel :
            if i in physique_en_raison_de_la_taille:
                if i in physique_localisé_en_dessous_de_la_taille:
                    if i in physique_localisé_au_dessus_de_la_taille:
                        c4_5_6_7.append(i)
        print(c4_5_6_7)

    #en cour...


    #5 options
    if c1==1 and c2==1 and c3==1 and c4==1 and c5==1 and c6!=1 and c7!=1 :
        c1_2_3_4_5=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in visuel:
                        if i in physique_en_raison_de_la_taille:
                            c1_2_3_4_5.append(i)
        print(c1_2_3_4_5)

    if c1==1 and c2==1 and c3==1 and c4==1 and c5!=1 and c6==1 and c7!=1 :
        c1_2_3_4_6=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in visuel:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            c1_2_3_4_6.append(i)
        print(c1_2_3_4_6)

    if c1==1 and c2==1 and c3==1 and c4==1 and c5!=1 and c6!=1 and c7==1 :
        c1_2_3_4_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in visuel:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_2_3_4_7.append(i)
        print(c1_2_3_4_7)

    if c1==1 and c2==1 and c3==1 and c4!=1 and c5==1 and c6==1 and c7!=1 :
        c1_2_3_5_6=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            c1_2_3_5_6.append(i)
        print(c1_2_3_5_6)

    if c1==1 and c2==1 and c3==1 and c4!=1 and c5==1 and c6!=1 and c7==1 :
        c1_2_3_5_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_2_3_5_7.append(i)
        print(c1_2_3_5_7)

    if c1==1 and c2==1 and c3==1 and c4!=1 and c5!=1 and c6==1 and c7==1 :
        c1_2_3_6_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_2_3_6_7.append(i)
        print(c1_2_3_6_7)

    if c1==1 and c2==1 and c3!=1 and c4==1 and c5==1 and c6==1 and c7!=1 :
        c1_2_4_5_6=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            c1_2_4_5_6.append(i)
        print(c1_2_4_5_6)

    if c1==1 and c2==1 and c3!=1 and c4==1 and c5==1 and c6!=1 and c7==1 :
        c1_2_4_5_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_2_4_5_7.append(i)
        print(c1_2_4_5_7)

    if c1==1 and c2==1 and c3!=1 and c4==1 and c5!=1 and c6==1 and c7==1 :
        c1_2_4_6_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in visuel:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_2_4_6_7.append(i)
        print(c1_2_4_6_7)

    if c1==1 and c2==1 and c3!=1 and c4!=1 and c5==1 and c6==1 and c7==1 :
        c1_2_5_6_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_2_5_6_7.append(i)
        print(c1_2_5_6_7)

    if c1==1 and c2!=1 and c3==1 and c4==1 and c5==1 and c6==1 and c7!=1 :
        c1_3_4_5_6=[]
        for i in cardiovasculaire :
            if i in cérébral:
                if i in visuel:
                    if i in  physique_en_raison_de_la_taille:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            c1_3_4_5_6.append(i)
        print(c1_3_4_5_6)

    if c1==1 and c2!=1 and c3==1 and c4==1 and c5==1 and c6!=1 and c7==1 :
        c1_3_4_5_7=[]
        for i in cardiovasculaire :
            if i in cérébral:
                if i in visuel:
                    if i in  physique_en_raison_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_3_4_5_7.append(i)
        print(c1_3_4_5_7)

    if c1==1 and c2!=1 and c3==1 and c4==1 and c5!=1 and c6==1 and c7==1 :
        c1_3_4_6_7=[]
        for i in cardiovasculaire :
            if i in cérébral:
                if i in visuel:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_3_4_6_7.append(i)
        print(c1_3_4_6_7)

    if c1==1 and c2!=1 and c3==1 and c4!=1 and c5==1 and c6==1 and c7==1 :
        c1_3_5_6_7=[]
        for i in cardiovasculaire :
            if i in cérébral:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_3_5_6_7.append(i)
        print(c1_3_5_6_7)

    if c1==1 and c2!=1 and c3!=1 and c4==1 and c5==1 and c6==1 and c7==1 :
        c1_4_5_6_7=[]
        for i in cardiovasculaire :
            if i in visuel:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c1_4_5_6_7.append(i)
        print(c1_4_5_6_7)

    if c1!=1 and c2==1 and c3==1 and c4==1 and c5==1 and c6==1 and c7!=1 :
        c2_3_4_5_6=[]
        for i in auditif:
            if i in cérébral:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            c2_3_4_5_6.append(i)
        print(c2_3_4_5_6)

    if c1!=1 and c2==1 and c3==1 and c4==1 and c5==1 and c6!=1 and c7==1 :
        c2_3_4_5_7=[]
        for i in auditif:
            if i in cérébral:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c2_3_4_5_7.append(i)
        print(c2_3_4_5_7)

    if c1!=1 and c2==1 and c3==1 and c4==1 and c5!=1 and c6==1 and c7==1 :
        c2_3_4_6_7=[]
        for i in auditif:
            if i in cérébral:
                if i in visuel:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c2_3_4_6_7.append(i)
        print(c2_3_4_6_7)

    if c1!=1 and c2==1 and c3==1 and c4!=1 and c5==1 and c6==1 and c7==1 :
        c2_3_5_6_7=[]
        for i in auditif:
            if i in cérébral:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c2_3_5_6_7.append(i)
        print(c2_3_5_6_7)

    if c1!=1 and c2==1 and c3!=1 and c4==1 and c5==1 and c6==1 and c7==1 :
        c2_4_5_6_7=[]
        for i in auditif:
            if i in visuel:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c2_4_5_6_7.append(i)
        print(c2_4_5_6_7)

    if c1!=1 and c2!=1 and c3==1 and c4==1 and c5==1 and c6==1 and c7==1 :
        c3_4_5_6_7=[]
        for i in cérébral:
            if i in visuel:
                if i in physique_en_raison_de_la_taille:
                    if i in physique_localisé_en_dessous_de_la_taille:
                        if i in physique_localisé_au_dessus_de_la_taille:
                            c3_4_5_6_7.append(i)
        print(c3_4_5_6_7)



    #6 options
    if c1==1 and c2==1 and c3==1 and c4==1 and c5==1 and c6==1 and c7!=1:
        c1_2_3_4_5_6=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in visuel:
                        if i in physique_en_raison_de_la_taille:
                            if i in physique_localisé_en_dessous_de_la_taille:
                                c1_2_3_4_5_6.append(i)
        print(c1_2_3_4_5_6)

    if c1==1 and c2==1 and c3==1 and c4==1 and c5==1 and c6!=1 and c7==1:
        c1_2_3_4_5_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in visuel:
                        if i in physique_en_raison_de_la_taille:
                            if i in physique_localisé_au_dessus_de_la_taille:
                                c1_2_3_4_5_7.append(i)
        print(c1_2_3_4_5_7)

    if c1==1 and c2==1 and c3==1 and c4==1 and c5!=1 and c6==1 and c7==1:
        c1_2_3_4_6_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in visuel:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            if i in physique_localisé_au_dessus_de_la_taille:
                                c1_2_3_4_6_7.append(i)
        print(c1_2_3_4_6_7)

    if c1==1 and c2==1 and c3==1 and c4!=1 and c5==1 and c6==1 and c7==1:
        c1_2_3_5_6_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            if i in physique_localisé_au_dessus_de_la_taille:
                                c1_2_3_5_6_7.append(i)
        print(c1_2_3_5_6_7)

    if c1==1 and c2==1 and c3!=1 and c4==1 and c5==1 and c6==1 and c7==1:
        c1_2_4_5_6_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            if i in physique_localisé_au_dessus_de_la_taille:
                                c1_2_4_5_6_7.append(i)
        print(c1_2_4_5_6_7)

    if c1==1 and c2!=1 and c3==1 and c4==1 and c5==1 and c6==1 and c7==1:
        c1_3_4_5_6_7=[]
        for i in cardiovasculaire :
            if i in cérébral:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            if i in physique_localisé_au_dessus_de_la_taille:
                                c1_3_4_5_6_7.append(i)
        print(c1_3_4_5_6_7)

    if c1!=1 and c2==1 and c3==1 and c4==1 and c5==1 and c6==1 and c7==1:
        c2_3_4_5_6_7=[]
        for i in auditif :
            if i in cérébral:
                if i in visuel:
                    if i in physique_en_raison_de_la_taille:
                        if i in physique_localisé_en_dessous_de_la_taille:
                            if i in physique_localisé_au_dessus_de_la_taille:
                                c2_3_4_5_6_7.append(i)
        print(c2_3_4_5_6_7)

    #7 options
    if c1==1 and c2==1 and c3==1 and c4==1 and c5==1 and c6==1 and c7==1:
        c1_2_3_4_5_6_7=[]
        for i in cardiovasculaire :
            if i in auditif:
                if i in cérébral:
                    if i in visuel:
                        if i in physique_en_raison_de_la_taille:
                            if i in physique_localisé_en_dessous_de_la_taille:
                                if i in physique_localisé_au_dessus_de_la_taille:
                                    c1_2_3_4_5_6_7.append(i)
        print(c1_2_3_4_5_6_7)



def open():
    #screen2
    essais=Toplevel()
    essais.geometry("1280x720")
    essais.title("Handisport")
    essais.configure(bg="lightblue")
    essais.iconbitmap("D:/Handisport/Dossier technique/Sources/logo sans handisport.ico")


    #titre
    label = Label(essais, text= "Quel est/sont ton/tes handicap(s) ?", height=2, width=100, bg="lightblue", font=("Castellar", 40))
    label.pack(pady=40)


    #checkliste
    c1 = Checkbutton(essais, text = "cardiovasculaire", height = 2, width = 50, font=("Arial",16), bg="lightblue",variable=choix1, onvalue=1, offvalue=0)
    c2 = Checkbutton(essais, text = "auditif", height = 2, width = 50, font=("Arial",16), bg="lightblue",variable=choix2)
    c3 = Checkbutton(essais, text = "cérébral", height = 2, width = 50,font=("Arial",16), bg="lightblue",variable=choix3)
    c4 = Checkbutton(essais, text = "visuel", height = 2, width = 50,font=("Arial",16), bg="lightblue",variable=choix4)
    c5 = Checkbutton(essais, text = "physique en raison de la taille", height = 2, width = 50,font=("Arial",16), bg="lightblue",variable=choix5)
    c6 = Checkbutton(essais, text = "physique localisé en dessous de la taille", height = 2, width = 50, font=("Arial",16), bg="lightblue", variable=choix6)
    c7 = Checkbutton(essais, text = "physique localisé au dessus de la taille", height = 2, width = 50, font=("Arial",16), bg="lightblue",variable=choix7)
    c1.pack()
    c2.pack()
    c3.pack()
    c4.pack()
    c5.pack()
    c6.pack()
    c7.pack()



    valider= Button(essais, text="VALIDER",activebackground="green", activeforeground="white", width=10,height= 2, font="Arial", bg="lightgreen", command=open2)
    valider.pack(pady=50)




#screen1
projet = tkinter.Tk()
projet.geometry("1280x720")
projet.title("Handisport")
projet.configure(bg="lightblue")
projet.iconbitmap("D:/Handisport/Dossier technique/Sources/logo sans handisport.ico")


#variable
choix1=IntVar()
choix2=IntVar()
choix3=IntVar()
choix4=IntVar()
choix5=IntVar()
choix6=IntVar()
choix7=IntVar()




#titre
l1 = Label(text="Handisport",bg="lightblue",font=("Castellar",70))
l1.pack(pady=40)

#bouton screen1
bouton1= Button(text="Trouves ton sport!",activebackground="black", activeforeground="white",width=25,height=1, font="Castellar", command=open)
bouton1.pack(pady=240)

projet.mainloop()

