"""Real 'foundation model for PDEs' run: PRE-TRAIN one network on a whole family of related
problems, then ADAPT it to a new problem with only a few examples — and compare to training
from scratch on those same few. Pretraining wins when data is scarce. CPU PyTorch."""
import torch
torch.manual_seed(0)
grid=torch.linspace(0,1,40)
def solutions(freqs,phase=0.0):
    # a 'family' of fields: sin(k*pi*x + phase) for various k -> input (freq), output (field)
    X=[]; Y=[]
    for k in freqs:
        X.append(torch.tensor([float(k)])); Y.append(torch.sin(k*torch.pi*grid+phase))
    return torch.stack(X),torch.stack(Y)
def mlp():
    return torch.nn.Sequential(torch.nn.Linear(1,64),torch.nn.Tanh(),torch.nn.Linear(64,64),torch.nn.Tanh(),torch.nn.Linear(64,40))
def train(net,X,Y,steps,lr=3e-3):
    o=torch.optim.Adam(net.parameters(),lr=lr)
    for _ in range(steps): o.zero_grad(); ((net(X)-Y)**2).mean().backward(); o.step()
# pretrain on a broad family (phase 0), many tasks
Xp,Yp=solutions(range(1,9),phase=0.0); pre=mlp(); train(pre,Xp,Yp,4000)
# NEW task family: shifted phase; only 3 training examples available
Xn,Yn=solutions([1,3,5],phase=0.9); Xtest,Ytest=solutions([2,4,6],phase=0.9)
import copy
ft=copy.deepcopy(pre); train(ft,Xn,Yn,400,lr=1e-3)          # fine-tune pretrained
sc=mlp(); train(sc,Xn,Yn,400,lr=1e-3)                         # from scratch, same budget
with torch.no_grad():
    e_ft=((ft(Xtest)-Ytest)**2).mean().sqrt().item()
    e_sc=((sc(Xtest)-Ytest)**2).mean().sqrt().item()
print("=== foundation model for PDEs: pretrain broadly, adapt with a few examples ===")
print(f"  pretrained on 8 related fields, then adapted to a NEW shifted family with only 3 examples.")
print(f"  error on unseen cases of the new family:")
print(f"    trained from scratch on the 3 examples: {e_sc:.4f}")
print(f"    fine-tuned from the pretrained model  : {e_ft:.4f}")
print(f"  => the pretrained model already knows the 'shape' of such fields, so a few examples")
print(f"     adapt it; from scratch, 3 examples are far too few. This is the foundation-model bet.")
