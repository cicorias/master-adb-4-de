# Databricks notebook source
class Config():    
    def __init__(self):
        # SPC: these are two external locations used for the "drop" and the "checkpoint" processing    
        self.base_dir_data = spark.sql("describe external location `data_zone`").select("url").collect()[0][0]
        self.base_dir_checkpoint = spark.sql("describe external location `checkpoint`").select("url").collect()[0][0]


        # SPC: the following is setting up just One schema --
        # SPC: we desire three schemas for "bronze, silver, gold"
        self.db_name = "sbit_db"  # this is the schema/database - term schema and db are synonyms in databricks and here.

        # SPC: alternatively -- for each bronze, silver, gold (silver and gold using atomic symbol of ag and au respectively)
        self.db_bz_name = "sbit_db_bz"
        self.db_ag_name = "sbit_db_ag"
        self.db_au_name = "sbit_db_au"

        self.maxFilesPerTrigger = 1000
