import numpy as np
import benchml as bml


if __name__ == "__main__":
    bml.log.Connect()
    bml.log.AddArg("models", (list,str), default=["^bmol_*.*_krr$"])
    bml.log.AddArg("meta_json", str, default="./meta.json")
    bml.log.AddArg("prefix", str, default="bml")
    
    args = bml.log.Parse()

    bml.readwrite.configure(use_ase=True)
    bml.splits.synchronize(seed=0)

    models = list(bml.models.compile_and_filter(["^bmol_.*$"], args.models))
    datasets = bml.data.DatasetIterator(meta_json=args.meta_json)
    print("using data set:", datasets)

    for data in datasets:
        kmat = {}
        for i, model in enumerate(models):
            stream = model.open(data)
            for train, test in stream.split(method="random", n_splits=1, train_fraction=min(0.9, 100./len(data))):
                model.fit(train, endpoint="kernel") # .fit rather than .map because some descriptors need to be "fitted"
                K = train.resolve('kernel.K')
                X = train.resolve('descriptor.X')
                print('< voila, the kernel for model %s' % model.tag)
                print(K.shape)
                kmat[model.tag] = K
                #np.savetxt('%s.kmat' % model.tag, K, fmt='%.8e')
                #print(X)
                #print(X.shape)
                #input('< voila, the kernel for model %s' % model.tag)
        
        k_model = np.ones((len(models),len(models)))
        name_model = []
        for i, model_i in enumerate(models):
            name_model.append(model_i.tag)
            for j, model_j in enumerate(models):
                if i > j:
                    kij = np.mean(np.multiply(np.asmatrix(kmat[model_i.tag]), np.asmatrix(kmat[model_j.tag])))
                    print("comparing ", model_i.tag, model_j.tag, "similarity = ", kij )
                    k_model[i,j] = k_model[j,i] = kij

    np.savetxt(args.prefix+'-descriptors.kmat', k_model, fmt='%.8e')
    np.savetxt(args.prefix+'-descriptors.names', name_model, fmt='%s')
    exit()

