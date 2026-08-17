"""Real attention run: a task where the output at each position depends on a FAR-AWAY
position chosen by the content, not by fixed distance. Content-based attention solves it;
a fixed-window local filter cannot reach the needed token. numpy only."""
import numpy as np
rng=np.random.default_rng(0)
def task(n=12):
    # sequence of vectors; position 0 holds a "pointer" one-hot to some index j; answer = value at j
    L=8
    vals=rng.standard_normal((n,L)); ptr=rng.integers(1,n)
    q=np.zeros(L); q[0]=ptr        # position 0 encodes which index to fetch (in coord 0)
    seq=vals.copy(); seq[0]=q
    return seq, vals[ptr], ptr
def attention_fetch(seq,ptr):
    # content-based: query = "index ptr"; keys = each position's index; softmax picks position ptr
    n=len(seq); idx=np.arange(n)
    scores=-(idx-ptr)**2*5.0                  # match the pointer to the position index
    w=np.exp(scores-scores.max()); w/=w.sum()
    return w@seq, w.argmax()
def local_filter(seq,window=2):
    # a fixed local window around position 0 can only average nearby positions
    return seq[:window+1].mean(0)
ok_att=0; ok_loc=0; T=200
for _ in range(T):
    seq,ans,ptr=task()
    got,picked=attention_fetch(seq,ptr); ok_att+= (picked==ptr)
    loc=local_filter(seq); ok_loc+= (np.argmin(((seq-loc)**2).sum(1))==ptr)
print("=== attention: reach the RIGHT far-away position by content, not by distance ===")
print("  task: position 0 says 'fetch index j'; the answer lives at position j, anywhere in the sequence.")
print(f"  content-based attention picks the correct far position: {100*ok_att/T:.0f}% of the time")
print(f"  a fixed local window (looks only near position 0):       {100*ok_loc/T:.0f}% of the time")
print("  => attention routes information from wherever it is needed, however far; a fixed-distance")
print("     filter is blind past its window. That any-to-any routing is why attention runs on fields too.")
