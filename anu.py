B
    ��\  �            	   @   s�   d dl mZ d dlZd dlZd dlZdZdZdZ	yd dl
Z
W n* ek
rf   ejddejejd� Y nX d	d
� Zdd� Zdd� Zedkr�e�  dS )�    )�compileNz[92mz[91mz[0mzpip install uncompyle6T)�shell�stdout�stderrc              C   s�   t �d� ttd t d � ttd t d � ttd t d � ttd t d	 � ttd
 t �} x8| dkr�| dkr�| dkr�ttd � ttd t �} qlW | dkr�t�  n(| dkr�t�  nttd t � t	�
�  d S )N�clearuc  
⢸⣗⡿⢸⡿P⡷⣏⡯⣟⣷Y⡧⣗⣯⣿⣟⣇T⣯⣷⡟⡟⢸⡗H⣗⡗⣏⡗⡷⣗O⣯⡿⣧N⡗⡏⡿⡏⢸⣏⣯
⡿⣗⣧C⡧⣟O⡏⣿⡟M⣏⡇⡿⡧⡟⡏P⣧⡗⡧Y⡷⣗L⣇⡟⡏⡟E⣿⡿⡿R⡯⣯⡿⡗⡏⡿⡏⢸⣏⣯
⡧⣟⡏⣯⡯⡿⣯⣿⡧⡇⡷⡷⡿⣇⡗⡏⡿⡏⢸⣏⣯⣟⡗⢸⡏⡯⡷⢸⡗⡷⡧⣗⣿⢸⣯⡇⡗⣇⡿⡯⡗⡏⡿⡏
⣟⡿⣯⣷⡇⡯⣇⡯⡷K⣿⣏⣧⡇a⣗⡧r⣟⡏⣿⣷⣧⣟j⡟⢸⢸⢸⡧⡇⣷o⣧⣇⣇⡿⡇k⡷⡧⣧⡷⣷
⡏⡇⡗⣷⡏⣟⡷⡗⡷⡧⢸⡗⡏⡿⡧⡗CRABS_ID⡗⡿⡏⣯⡏⡏⡧⣟⡟⢸⣏⡷⣧⡧⡯⡇⣏⡏⡗⡏
 z*h t t p s : / / t . m e / C R A B S _ I D
z1.z	 Compylerz2.z Uncompylerz0.z Minggatz
Mau ngapain gayn ? : �1�2�0zemmuach ! :* zMau ngapain gayn ? : zOke, lu burrique, gw gans. tq)�os�system�print�h�m�x�input�karjok�pangesty�sys�exit)�ops� r   �kompiler.py�pejuang_ldr   s"    

r   c           
   C   sF  t td t �} | �d�d }| dkr0t��  n yt| � W n( tk
rd   tt	d � t��  Y nX y�t
�d| d | d � t
�d| d	 � ttd
 � ttd t | d � tt	d � t t	d t �}|dkr�t�  nt�  W nT tk
�r@ } z4t|� t td t �}|dk�r*t�  nt�  W d d }~X Y nX d S )Nz
Nama file: �.r   � �nullbytezcd __pycache__ && mv z.cpython-37.pyc z_terkompile.pyz_terkompile.py ..zoke gayn.. sukses !z	hasilnya z++++++++++++++++++++++++++++++++++++++++++++zlagi ? y/n: �y)r   r   r   �splitr   r   �c�
ValueErrorr   r   r
   r   r   r   �	Exception)�z�nf�ask�ser   r   r   r   *   s2    


r   c           	   C   sz  t td t �} | �d�d }d| ks.d| krpt�d� t td t �}|dkrdxttd	 � qRW nt�	�  �n| d
kr�t�	�  n�yt�
d� W n tk
r�   Y nX t�d|  d � t�d|  d | d � d|  }t|d d��}tj|d|d� W d Q R X ttd � ttd t | d � ttd � |��  t td t �}|dk�r^t�  nt�d| d � t�  d S )Nz
Nama file: r   r   zsytd.pyzanu.pyr   ztAnda mencoba menguncompyle file terkontaminasi virus.
yakin ingin lanjut ?
(mungkin file system akan terhapus) y/n: r   u�  ⢸⣗⡿⢸⡿P⡷⣏⡯⣟⣷Y⡧⣗⣯⣿⣟⣇T⣯⣷⡟⡟⢸⡗H⣗⡗⣏⡗⡷⣗O⣯⡿⣧N⡗⡏⡿⡏⢸⣏⣯⡿⣗⣧C⡧⣟O⡏⣿⡟M⣏⡇⡿⡧⡟⡏P⣧⡗⡧Y⡷⣗L⣇⡟⡏⡟E⣿⡿⡿R⡯⣯⡿⡗⡏⡿⡏⢸⣏⣯⡧⣟⡏⣯⡯⡿⣯⣿⡧⡇⡷⡷⡿⣇⡗⡏⡿⡏⢸⣏⣯⣟⡗⢸⡏⡯⡷⢸⡗⡷⡧⣗⣿⢸⣯⡇⡗⣇⡿⡯⡗⡏⡿⡏⣟⡿⣯⣷⡇⡯⣇⡯⡷K⣿⣏⣧⡇a⣗⡧r⣟⡏⣿⣷⣧⣟j⡟⢸⢸⢸⡧⡇⣷o⣧⣇⣇⡿⡇k⡷⡧⣧⡷⣷⡏⡇⡗⣷⡏⣟⡷⡗⡷⡧⢸⡗⡏⡿⡧⡗CRABS_ID⡗⡿⡏⣯⡏⡏⡧⣟⡟⢸⣏⡷⣧⡧⡯⡇⣏⡏⡗⡏h t t p s : / / t . m e / C R A B S _ I Dr   �__pycache__zcp z __pycache__zcd __pycache__ && mv � z.cpython-37.pyczuncompyle6 z_terUncompile.py�wT)r   r   zmantab gayn.. unkompil sukses !z	hasilnya z++++++++++++++++++++++++++++++++++++++++++++zlagi ? y/n: zcd __pycache__ && rm )r   r   r   r   r
   r   r   r   r   r   �mkdir�OSError�open�sp�call�closer   r   )r!   r"   �tny�fl�or#   r   r   r   r   R   s:    


r   �__main__)�
py_compiler   r   �
subprocessr+   r
   r   r   r   r   �
uncompyle6�ModuleNotFoundErrorr,   �DEVNULL�STDOUTr   r   r   �__name__r   r   r   r   �<module>   s   ($