import pandas as pd
from pathlib import Path


def load_csv(path: Path, **kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **kwargs)

def save_csv(df: pd.DataFrame, path: Path, index: bool = False):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)

def load_data(path: Path, **kwargs) -> pd.DataFrame:
    """
    Carrega dados detectando o formato pela extensão.
    Tenta Parquet (Zstd) por padrão se for .parquet.
    """
    if path.suffix.lower() == '.csv':
        try:
            return pd.read_csv(path, **kwargs)
        except Exception as e:
            print(f"Erro ao ler CSV em {path}: {e}")
            raise
    
    # Se não for CSV, assume Parquet com Zstd
    try:
        return pd.read_parquet(path, engine='pyarrow', **kwargs)
    except Exception as e:
        print(f"Erro ao ler Parquet em {path}: {e}")
        raise

def save_data(df: pd.DataFrame, path: Path, index: bool = False, **kwargs):
    """
    Salva os dados em formato Parquet com compressão Zstandard.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Garante que a extensão seja .parquet para não confundir depois
    if path.suffix.lower() != '.parquet':
        path = path.with_suffix('.parquet')
        
    print(f"Salvando: {path} (Compressão: Zstd)")
    df.to_parquet(path, index=index, compression="zstd", engine='pyarrow', **kwargs)    