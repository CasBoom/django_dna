from django.db import models
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Create your models here.

class dna_profile(models.Model):
    title = models.CharField(max_length=200)
    dna = models.TextField()
    
    def size(self):
        return len(self.dna)

    # returns a dataframe containing the amount of each nucleobase
    def count_nucleobases(self):
        adenine = 0
        thymine = 0
        cytosine = 0
        guanine = 0
        for nucleobase in self.dna:
            if(nucleobase == 'A'):
                adenine+=1
            elif(nucleobase == 'T'):
                thymine+=1
            elif(nucleobase == 'C'):
                cytosine+=1
            elif(nucleobase == 'G'):
                guanine+=1

        return [adenine,cytosine,guanine,thymine]


    def df_nucleobase_count(self):
        data = {'Nucleobase':['Adenine','Cytosine','Guanine','Thymine'],
                'Frequency':self.count_nucleobases()}
        df = pd.DataFrame(data).to_html()
        return df
        # return df.plot.bar(x="Nucleobase", y="Frequency", rot=70, title="Nucleobase count")

    def find_gc(self):
        total_amount = 0
        gc_count = 0
        if(len(self.dna) <= 0):
            return 100
        else:
            for nucleobase in self.dna:
                total_amount+=1
                if (nucleobase == 'G') or (nucleobase == 'C'):
                    gc_count += 1
            return np.round((gc_count / total_amount)*100, 6)

    def count_point_mutations(self, other_dna):
        m = 0
        if(len(self.dna[i]) <= other_dna[i]):
            for i in range(0, len(self.dna_1)-1):
                if self.dna[i] != other_dna[i]:
                    m+=1
        else:
            for i in range(0, len(other_dna)-1):
                if self.dna[i] != other_dna[i]:
                    m+=1
        return m

    def reverse_compliment(self):
        output = ""
        for nucleobase in self.dna:
            if nucleobase == "A":
                output = "T" + output
            elif nucleobase == "T":
                output = "A" + output
            elif nucleobase == "G":
                output = "C" + output
            elif nucleobase == "C":
                output = "G" + output
        return output

    def find_rna(self):
        rna = ""
        for letter in self.dna:
            if letter == "T":
                rna = rna + "U"
            else:
                rna = rna + letter
        return rna

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:2000]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')