import ast
from typing import List, Tuple, Optional


def extract_arguments(file_path: str) -> Tuple[Optional[str], Optional[str], List[
    Tuple[str, Optional[str], Optional[str], Optional[str], Optional[bool], Optional[str], Optional[list]]]]:
    """
    Filters program name, description and arguments from the given python script.

    Args:
        file_path:          Path to the python script.

    Returns:
        prog_name:          Program name.
        prog_description:   Program description.
        arguments:          List of arguments.
    """

    prog_name = None
    prog_description = None
    args = []

    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), filename=file_path)

    class ArgumentVisitor(ast.NodeVisitor):
        """
        Extracts program name, description and arguments from the given python script.
        """
        def __init__(self):
            self.parsers = {}

        def visit_Assign(self, node: ast.Assign):
            """
            Processes Assign nodes in the AST tree.

            This function will extract `prog` and `description` variables from the given
            python script. It will also extract information from the ArgumentParser
            constructor. That information will be stored in the `parsers` dictionary.

            Args:
                node:       The Assign node to be processed.
            """
            try:
                nonlocal prog_name, prog_description
                if isinstance(node.targets[0], ast.Attribute) and isinstance(node.value, ast.Str):
                    if node.targets[0].attr == 'prog':
                        prog_name = node.value.s
                    elif node.targets[0].attr == 'description':
                        prog_description = node.value.s
            except Exception as e:
                print(f"Error processing node: {e}")

            if isinstance(node.value, ast.Call) and isinstance(node.value.func,
                                                               ast.Name) and node.value.func.id == 'ArgumentParser':
                parser_name = node.targets[0].id if isinstance(node.targets[0], ast.Name) else None
                if parser_name:
                    parser_info = {}
                    for keyword in node.value.keywords:
                        print('xd')
                        if keyword.arg == 'description':
                            parser_info['description'] = keyword.value.s if isinstance(keyword.value, ast.Str) else None
                        elif keyword.arg == 'prog':
                            parser_info['prog'] = keyword.value.s if isinstance(keyword.value, ast.Str) else None
                    self.parsers[parser_name] = parser_info
            self.generic_visit(node)

        def visit_Call(self, node: ast):
            """
            Processes Call nodes in the AST tree.

            This function will extract information from `add_argument` method calls.
            It will extract the argument name, default value, help text, type, required
            status, action, and choices from the `add_argument` call. This information
            will be stored in the `args` list.

            Args:
                node:       The Call node to be processed.
            """
            if isinstance(node.func, ast.Attribute) and node.func.attr == 'add_argument':
                parser_name = node.func.value.id if isinstance(node.func.value, ast.Name) else None
                parser_info = self.parsers.get(parser_name, {})
                arg_name = None
                arg_name_2 = None
                if node.args:
                    arg_name = node.args[0].s if isinstance(node.args[0], ast.Str) else None
                try:
                    if node.keywords:
                        arg_name_2 = node.args[1].s if isinstance(node.args[1], ast.Str) else None
                except IndexError:
                    pass
                default = None
                help_text = None
                arg_type = None
                required = False
                action = None
                choices = []
                for keyword in node.keywords:
                    if keyword.arg == 'default':
                        if isinstance(keyword.value, ast.Str):
                            default = keyword.value.s
                        elif isinstance(keyword.value, ast.Num):
                            default = keyword.value.n
                        elif isinstance(keyword.value, ast.NameConstant):
                            default = keyword.value.value
                    elif keyword.arg == 'help':
                        if isinstance(keyword.value, ast.Str):
                            help_text = keyword.value.s
                    elif keyword.arg == 'type':
                        if isinstance(keyword.value, ast.Name):
                            arg_type = keyword.value.id
                    elif keyword.arg == 'required':
                        if isinstance(keyword.value, ast.NameConstant):
                            required = keyword.value.value
                    elif keyword.arg == 'action':
                        if isinstance(keyword.value, ast.Str):
                            action = keyword.value.s
                    elif keyword.arg == 'choices':
                        if isinstance(keyword.value, ast.List):
                            choices = [elt.s for elt in keyword.value.elts if isinstance(elt, ast.Str)]
                if arg_name:
                    args.append((arg_name, arg_name_2, default, help_text, arg_type, required, action, choices))
            self.generic_visit(node)

    visitor = ArgumentVisitor()
    visitor.visit(tree)
    return prog_name, prog_description, args
