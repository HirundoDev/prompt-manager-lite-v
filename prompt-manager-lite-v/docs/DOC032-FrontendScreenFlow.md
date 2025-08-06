# DOC032: Flujo de Pantallas y Rutas del Frontend

> **Propósito:** Este documento mapea cada pantalla o vista de la interfaz de usuario a sus componentes de código, rutas y las APIs que consume. Es una referencia cruzada esencial para entender el flujo de datos y la interacción en el frontend.

---

## 1. Pantalla: [Nombre de la Pantalla, ej: 'Login']

- **Ruta de Acceso:** `/login`
- **Componente Principal:** `src/views/LoginView.vue`
- **Componentes Secundarios:**
  - `src/components/LoginForm.vue`
  - `src/components/ui/PrimaryButton.vue`
- **APIs Consumidas:**
  - `POST /api/auth/login`: Para autenticar al usuario.
  - `GET /api/users/me`: Para obtener datos del perfil tras el login.
- **Flujo de Navegación:**
  - **Al éxito:** Redirige a `/dashboard`.
  - **Al fallo:** Muestra el componente `src/components/ErrorModal.vue`.

---

## 2. Pantalla: [Nombre de la Pantalla, ej: 'Dashboard']

- **Ruta de Acceso:** `/dashboard`
- **Componente Principal:** `src/views/DashboardView.vue`
- **Componentes Secundarios:**
  - `src/components/ProjectList.vue`
  - `src/components/SidebarNav.vue`
- **APIs Consumidas:**
  - `GET /api/projects`: Para listar los proyectos del usuario.
- **Flujo de Navegación:**
  - **Click en proyecto:** Redirige a `/projects/:id`.

---