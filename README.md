# Python Backstage Components

Repository created for generating instances in Backstage using jinja2.

> :memo: **Note:** Generation of components is only possible for those present in the software catalog.


## Usage

An example of usage is for the action of instantiating a new user, as shown below.

**1. Import the environment where the template is applied (in this case, it is the Software Catalog)**

```python
from Backstage import SoftwareCatalog
```
**2. Instantiate the manager and the template (both are general variables of the application)**

```python
manager = SoftwareCatalog.SoftwareCatalogManager()
template = SoftwareCatalog.Template
```

**3. Select the user template and add a 'name' attribute**

```python 
user_template = template.User()
instance = user_template.new(name='Natan')
```

* To instantiate other attributes, just call them in the function
```python 
user_template.new(...)
```
Refer to the documentation at [Backstage Docs](https://backstage.io/docs/features/software-catalog/descriptor-format) for more details.

**4. Finally, render**

```python 
rendered_instance = manager.match(instance)

print(rendered_instance)
```

The output will be something like:

```yaml
apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: Natan
  namespace: <class 'jinja2.utils.Namespace'>
spec:
```

The application architecture has the following format::
![arquitetura](https://drive.google.com/uc?id=1lyjfQvPkVSy7uObrcS82H8YJJZYUTt78)