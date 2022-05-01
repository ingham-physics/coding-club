# Optimisation examples

this folder contains a few examples of optimisation with python.

We can define 'optimisation' as the process of searching for some parameters that best meet some criteria'. Like any other search you might carry out, there are going to be a few considerations:

- You want the search to be as quick as possible
- You want the search to be as efficient as possible 

The approach that will help you find the best parameters quickly and efficiently is extremely situation dependant! I am going to cover a few practical examples that I have come across during my career.

I think these two examples are interesting because they are at opposite ends of the spectrum.

## Linear programming examples

https://realpython.com/linear-programming-python/

Linear programming is an extremely fast optimisation technique that can be applied when you know that every parameter you are optimising produces a linear response in your objective function. There are actually a surprisingly large number of situations where this is useful! 

- Even when the problem is not linear, it's often a good idea to start out by approximating it as a linear problem.
- Pretty much everything is linear in a small enough region! 

### Fluence optimisation in radiation therapy 

In radiation therapy, each treatment plan must be optimised for each patient. 

For simplicity, consider just one beam angle. We use the MLC to split the broad beam into multiple small 'beamlets'. Assume that we can perfectly split the broad beam into N beamlets. We now use some dose calculation algorithm (monte carlo, pencil beam, whatever) to calculate the dose map in the patient of each beamlet. **since the total dose from each beamlet is a linear function, we can use linear optimisation to find out how we should weight each of these beamlets**. This process is known as fluence optimisation.

The extension to multiple beams is trivial; the optimiser doesn't actually know what angle a beamlet comes from anyway - all it knows is what happens when it turns that beamlet up!

What is less trivial is actually figuring out how to deliver this optimised fluence! but that is not a topic for today. 

### Designing a passive magnetic shim for MRI

In MRI, it is integral to produce an extremely homogeneous field at the centre of the magnet. In practice, a variety of factors such as manufacturing tolerance and (particularly) environmental steel present at the installation mean that when a new magnet is installed, the homogeneity is always much worse than planned.

To compensate for this, a process known as 'passive shimming' is carried out. Passive shimming involves the careful placement of many pieces of iron inside the bore, in such a way that perturbation within the main magnetic field is minimised. 

**The effect of placing iron in a given location varies linearly as a function of the thickness of that iron.** This means that if we have some existing 'response matrix' that tells us the effect of a piece of iron, and we know what overall field we want to produce we can use linear optimisation to figure out the right thickness of all the iron pieces! 

### Preliminary design of MRI magnet



## Bayesian Optimisation examples

https://cs.lbl.gov/assets/CSSSP-Slides/20180719-Mueller.pdf

### Tuning parameters within Monte Carlo simulations

In  Medical  Physics,  Monte  Carlo  simulations  of radiation transport are  used  for  research  studies,  engineering designs, as a secondary dose check, and, increasingly, as a primary clinical dose calculation mechanism.

General purpose monte carlo is a computationally expensive process. 





### Design of experiments

