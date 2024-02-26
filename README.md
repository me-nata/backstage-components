# Python Backstage Components

Repositório criado para geração de instancias no Backstage a partir do jinja2.

> :memo: **Note:** Apenas é possível a geração de componentes presentes no software catalog.


## Usage

Um exemplo de uso é para a ação de instanciar um novo usuário como é possível ver abaixo

**1. Importamos o ambiente onde o template é aplicado (nesse caso é o Software Catalog)**

```python
from Backstage import SoftwareCatalog
```
**2. Instanciamos o manager e o template (ambos variáveis gerais da aplicação)**

```python
manager = SoftwareCatalog.SoftwareCatalogManager()
template = SoftwareCatalog.Template
```

**3. Selecionamos o template usuário e colocamos um atributo 'name'**

```python 
user_template = template.User()
instance = user_template.new(name='Natan')
```

* Para instanciar outros atributos, basta chamá-los na função
```python 
user_template.new(...)
```
Acompanhando a documentação, acesse [Backstage Docs](https://backstage.io/docs/features/software-catalog/descriptor-format)

**4. Por fim, renderizamos**

```python 
rendered_instance = manager.match(instance)

print(rendered_instance)
```

A saída será algo do tipo:

```yaml
apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: Natan
  namespace: <class 'jinja2.utils.Namespace'>
spec:
```

A arquitetura da aplicação apresenta o seguinte formato:
![arquitetura](https://drive.google.com/uc?id=1lyjfQvPkVSy7uObrcS82H8YJJZYUTt78)