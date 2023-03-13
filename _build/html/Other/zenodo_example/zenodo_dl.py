"""
Copyright 2020, LUMICKS B.V.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:
 
1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import os
import hashlib
import requests
from tqdm.auto import tqdm


def get_record_from_doi(doi):
    """Obtains a Zenodo record from the DOI (e.g. 10.5281/zenodo.#)"""
    url = doi if doi.startswith("http") else "https://doi.org/" + doi
    response = requests.get(url)
    
    if not response.ok:
        raise ValueError(f"DOI could not be resolved {response}")
        
    return response.url.split("/")[-1].strip()


def download_record_metadata(record_number):
    """Download specific Zenodo record metadata"""
    zenodo_url = "https://zenodo.org/api/records/"
    response = requests.get(zenodo_url + str(record_number))
    if response.ok:
        return response.json()
    else:
        raise ValueError(f"Failed to access Zenodo record {response}")

        
def download_file(url, file_name, block_size=4096):
    """Stream a file from a URL while showing progress"""
    response = requests.get(url, stream=True)
    size_bytes = int(response.headers.get("content-length", 0))

    dir_name = os.path.dirname(file_name)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
        
    with open(file_name, "wb") as file:
        with tqdm(total=size_bytes, unit="iB", unit_scale=True, desc=f"Download {file_name}") as progress_bar:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)


def verify_hash(file_name, algorithm, reference_hash, chunk_size=65536):
    """Verify the hash of a file"""
    size_bytes = int(os.path.getsize(file_name))
    
    m = hashlib.new(algorithm)
    with open(file_name, "rb") as f:
        with tqdm(total=size_bytes, unit="iB", unit_scale=True, desc=f"Verifying hash {file_name}") as progress_bar:
            b = f.read(chunk_size)
            while len(b) > 0:
                m.update(b)
                progress_bar.update(len(b))
                b = f.read(chunk_size)
            
    return m.hexdigest() == reference_hash


def download_from_doi(doi, force_download=False):
    """Download files from a Zenodo DOI (i.e. 10.5281/zenodo.#######) and returns a file list in the form of a
    List[str].
    
    Parameters
    ----------
    doi : str
        DOI of the files to download.
    force_download : bool
        Force re-downloading the file even if it already exists and the hash checks out."""
    rec = download_record_metadata(get_record_from_doi(doi))
    
    print(f"Fetching '{rec['metadata']['title']}'")
    file_names = []
    for file in rec["files"]:
        file_name, url = file["key"], file["links"]["self"]
        hash_algorithm, checksum = file["checksum"].split(':')

        skip = not force_download

        # If the file doesn't exist, we can't skip it
        if not os.path.exists(file_name):
            skip = False

        # If the file is not the one we want, we can also not skip it (only check the hash if the file exists)
        if skip and not verify_hash(file_name, hash_algorithm, checksum):
            print("Hash does not check out. Downloading file again")
            os.remove(file_name)
            skip = False

        if not skip:
            download_file(url, file_name)
            if not verify_hash(file_name, hash_algorithm, checksum):
                raise RuntimeError("Failed to validate checksum hash")
        else:
            print("File already exists and will not be downloaded again.")
                
        file_names.append(file_name)
        
    return file_names
