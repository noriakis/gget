import uuid

# Ensembl REST API server for gget seq and info
ENSEMBL_REST_API = "http://rest.ensembl.org/"
ENSEMBL_FTP_URL = "http://ftp.ensembl.org/pub/"
ENSEMBL_FTP_URL_PLANT = "http://ftp.ensemblgenomes.org/pub/plants/"

# NCBI URL for gget info
NCBI_URL = "https://www.ncbi.nlm.nih.gov"

# UniProt REST API server for gget seq and info
UNIPROT_REST_API = "https://rest.uniprot.org/uniprotkb/search?query="
UNIPROT_IDMAPPING_API = "https://rest.uniprot.org/idmapping"

# RCSB PDB API for gget pdb
RCSB_PDB_API = "https://data.rcsb.org/rest/v1/core/"

# API to get PDB entries from Ensembl IDs
ENS_TO_PDB_API = "https://www.ebi.ac.uk/pdbe/aggregated-api/mappings/ensembl_to_pdb/"

# BLAST API endpoints
BLAST_URL = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"
# Generate a random UUID
BLAST_CLIENT = "gget_client-" + str(uuid.uuid4())

# MUSCLE Github repo
MUSCLE_GITHUB_LINK = "https://github.com/rcedgar/muscle.git"

# Enrichr API endpoints
POST_ENRICHR_URL = "https://maayanlab.cloud/speedrichr/api/addList"
GET_ENRICHR_URL = "https://maayanlab.cloud/speedrichr/api/enrich"
POST_BACKGROUND_ID_ENRICHR_URL = "https://maayanlab.cloud/speedrichr/api/addbackground"
GET_BACKGROUND_ENRICHR_URL = "https://maayanlab.cloud/speedrichr/api/backgroundenrich"

# ARCHS4 API endpoints
GENECORR_URL = "https://maayanlab.cloud/matrixapi/coltop"
EXPRESSION_URL = "https://maayanlab.cloud/archs4/search/loadExpressionTissue.php?"

#ELM API endpoints
GET_ELM_API =  "http://elm.eu.org/start_search/"

#ELM URL for web scraping in gget elm
ELM_URL = "http://elm.eu.org/elms/"