import os
import sqlite3
from typing import Dict,List,Any

class StorageEngine:
    def __init__(self,db_name:str=".dsa_profile_history.db"):
        self.db_name=db_name
        self._initialize_db()
        
    def _get_connection(self)->sqlite3.Connection:
        return sqlite3.connect(self.db_name)
    
    def _initialize_db(self)->None:
        schema="""
        CREATE TABLE IF NOT EXISTS dsa_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem_id TEXT NOT NULL,
            run_name TEXT NOT NULL,
            execution_time_ms REAL NOT NULL,
            peak_memory_mb REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        with self._get_connection() as conn:
            cursor=conn.cursor()
            cursor.execute(schema)
            conn.commit()
            
    def save_run(self,problem_id:str,run_name:str,time_ms:float,memory_mb:float)->None:
        
        query="""
        INSERT INTO dsa_runs (problem_id,run_name,execution_time_ms,peak_memory_mb) VALUES (?,?,?,?)
        """
        
        with self._get_connection() as conn:
            cursor=conn.cursor()
            cursor.execute(query,(problem_id,run_name,time_ms,memory_mb))
            conn.commit()
            
    def get_history(self,problem_id:str)->List[Dict[str,Any]]:
        
        query="""
        SELECT run_name,execution_time_ms,peak_memory_mb,timestamp FROM dsa_runs WHERE problem_id = ? 
        ORDER BY timestamp ASC;
        """
        with self._get_connection() as conn:
            conn.row_factory=sqlite3.Row
            cursor=conn.cursor()
            cursor.execute(query,(problem_id,))
            
            rows=cursor.fetchall()
            return [dict(row) for row in rows]
        
        
        
        