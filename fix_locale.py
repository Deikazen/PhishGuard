import onnx

model_path = "model/tfidf.onnx"
model = onnx.load(model_path)

modified = False
for node in model.graph.node:
    if node.op_type == "StringNormalizer":
        has_locale = False
        for attr in node.attribute:
            if attr.name == "locale":
                attr.s = b"C"
                has_locale = True
                modified = True
                print("Modified existing locale attribute to 'C'.")
        
        if not has_locale:
            new_attr = onnx.helper.make_attribute("locale", b"C")
            node.attribute.append(new_attr)
            modified = True
            print("Added 'locale' attribute with value 'C'.")

if modified:
    onnx.save(model, model_path)
    print("Saved modified ONNX model.")
