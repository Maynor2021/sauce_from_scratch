import pytest
@pytest.mark.parametrize(
    "usuario, clave, error_esperado",                          # ① nombres de parámetros
    [                                                          # ② la tabla de casos
        ("standard_user", "clave_mala", "do not match"),
        ("locked_out_user", "secret_sauce", "locked out"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],                                                         #    ← cierra la lista, coma
    ids=["clave_incorrecta", "usuario_bloqueado", "sin_usuario", "sin_clave"],   # 
)          
@pytest.mark.regression
def test_login_fallido(login_page, usuario, clave, error_esperado):
    login_page.login(usuario, clave)
    assert error_esperado in login_page.get_error_message()