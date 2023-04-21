def compare_dicts(base, eval):
    return {k: {"base": base[k], "eval": eval[k]} for k in base if k in eval and base[k] != eval[k]}

def cross_compare(base_lemmas, eval_lemmas):
    pass
