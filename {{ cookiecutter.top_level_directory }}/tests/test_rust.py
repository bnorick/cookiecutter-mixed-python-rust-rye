import {{ cookiecutter.package_name }}


def describe_nominal():

    def with_foobar(expect):
        expect({{ cookiecutter.package_name }}.is_foobar("foobar")).is_(True)
        expect({{ cookiecutter.package_name }}.is_foobar("foodbard")).is_(False)
