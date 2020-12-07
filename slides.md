---
theme: gaia
backgroundColor: white
paginate: true
footer: Thomas Demarcy's interview @ Caranx Medical
---

# Contents
1. My background
2. Work philosophy
3. Project demo or code/architecture review
4. Questions

slide deck source: [github.com/tdemarcy/slides-2020-12-07](https://github.com/tdemarcy/slides-2020-12-07)

---
<!-- _class: lead -->

# 1. My background

---

# Profile analysis

![bg right contain](profile.svg)

Ask my referals:
- Nicholas Ayache
- Hervé Delingette
- Dan Gnansia
- Cédric Briand
- Benjamin Braga
- Jan Margeta

---

# Achievements

1. Bringing a new approach at Oticon Medical

---

## Oticon Medical

* Neurelec until 2013 (PhD 1st year)
* Hardware company
* Less than 10% of market share

---

## Data-driven approach
Throughout the product life cycle:

conception → implantation → fitting

---

## How?
[x] Preop. anatomy reconstruction (PhD, using Bayesian inference)
    → Surgery planning
[x] Postop. electrode reconstruction
    → Design review
[x] Modality registration
    → Insertion depth and trauma evaluation
[x] Fitting (Hz, nC) using images, impedences and demographics data
[  ] Nerve health modelisation using objective measures (e.g. eCAPs)

---

## Press

![bg 60%](MM29.svg)

---

# Achievements

1. Bringing a new approach at Oticon Medical
2. Initial technological design choices approved a posteriori by top management

---

## Technological design

* Use of actively maintained, cross-platform, multiple programming languages (C++, Python, JavaScript, etc.) libraries
* Cloud-based and GDPR compliant
* DevOps automation: Automated testing and container deployment, scaling, and management

---

## Why leaving Oticon Medical?

![bg 60%](anywhere.svg)

---
<!-- _class: lead -->

# 2. Work philosophy

---

## Quick-and-dirty?

![bg right contain](time.svg)

- quick prototyping
- short-term and long-term velocity
- needs for documentation

---

## Accuracy vs. Robustness

```python
n_sample = 100
error = pd.DataFrame(
    {
        "σ=0.1, df=1": random.standard_t(1, n_sample) * 0.1,
        "σ=1, df=10": random.standard_t(10, n_sample) * 1,
    }
)
abs_error = pd.melt(np.abs(error), var_name="method", value_name="absolute error")

plot_values = {"x": "method", "y": "absolute error", "data": abs_error}
sns.boxplot(**plot_values, **box_options)
sns.stripplot(**plot_values, **strip_options)
```

---

## Accuracy vs. Robustness

![60%](error.svg)
*valid for medical UX

---

## From MIC to CAI

![20%](http://www.miccai.org/themes/customtheme/images/MICCAI_logo_bkg.png)
Medical Image Computing and Computer Assisted Interventions

---

## My 2 keywords rule

![bg right:50% 80%](http://darcylab.com/assets/img/full.svg)

<br />

- **Computer vision**
`or`
- **Medical device**
`or`
- **Data science**

---
<!-- _backgroundColor: black -->
<!-- _paginate: false -->