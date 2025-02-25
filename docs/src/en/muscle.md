> Python arguments are equivalent to long-option arguments (`--arg`), unless otherwise specified. Flags are True/False arguments in Python. The manual for any gget tool can be called from the command-line using the `-h` `--help` flag.  
## gget muscle 🦾
Align multiple nucleotide or amino acid sequences to each other using [Muscle5](https://www.drive5.com/muscle/).  
Return format: ClustalW formatted standard out or aligned FASTA (.afa).  

**Positional argument**  
`fasta`   
Path to FASTA or .txt file containing the nucleotide or amino acid sequences to be aligned.  

**Optional arguments**  
`-o` `--out`   
Path to the aligned FASTA file the results will be saved in, e.g. path/to/directory/results.afa. Default: Standard out.   
Python: `save=True` will save the output in the current working directory.

**Flags**  
`-s5` `--super5`  
Aligns input using the [Super5 algorithm](https://drive5.com/muscle5/Muscle5_SuppMat.pdf) instead of the [Parallel Perturbed Probcons (PPP) algorithm](https://drive5.com/muscle5/Muscle5_SuppMat.pdf) to decrease time and memory.  
Use for large inputs (a few hundred sequences).

`-q` `--quiet`   
Command-line only. Prevents progress information from being displayed.  
Python: Use `verbose=False` to prevent progress information from being displayed. 
  
  
### Example
```bash
gget muscle fasta.fa
```
```python
# Python
gget.muscle("fasta.fa")
```
&rarr; Returns an overview of the aligned sequences with ClustalW coloring. (To return an aligned FASTA (.afa) file, use `--out` argument (or `save=True` in Jupyter Lab/Google Colab).) In the above example, the 'fasta.fa' includes several sequences to be aligned (e.g. isoforms returned from `gget seq`). 

![alt text](https://github.com/pachterlab/gget/blob/main/figures/example_muscle_return.png?raw=true)

#### [More examples](https://github.com/pachterlab/gget_examples)
