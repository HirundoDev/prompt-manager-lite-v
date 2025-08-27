<script>
	import { onMount, getContext } from 'svelte';
	import { invoke } from '../../lib/utils/tauri.js';
	import { Settings, Save, RefreshCw, User, FileText, Palette, Database, Shield, Plus, Upload } from 'lucide-svelte';
	import HelpIcon from '../../lib/components/HelpIcon.svelte';
	import HelpTooltip from '../../lib/components/HelpTooltip.svelte';

	// Contexto de ayuda
	const help = getContext('help');

	let settings = {
		theme: 'light',
		notifications: true,
		autoSave: true,
		language: 'es',
		projectPath: '/home/user/projects',
		backupEnabled: false
	};

	let loading = false;

	async function saveSettings() {
		loading = true;
		try {
			await invoke('save_settings', { settings });
			// Mostrar notificación de éxito
		} catch (error) {
			console.error('Error guardando configuración:', error);
		} finally {
			loading = false;
		}
	}
</script>

<div class="p-6">
	<div class="mb-6">
		<h1 class="text-2xl font-bold text-gray-900 dark:text-white flex items-center">
			<Settings class="w-6 h-6 mr-2" />
			Configuración
		</h1>
		<p class="text-gray-600 dark:text-gray-400 mt-2">
			Personaliza tu experiencia con The Mighty Task
		</p>
	</div>

	<div class="max-w-4xl space-y-8">
		<!-- Configuración de Apariencia -->
		<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
			<h2 class="text-lg font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
				<Palette class="w-5 h-5 mr-2" />
				Apariencia
			</h2>
			<div class="space-y-4">
				<div>
					<label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
						Tema
					</label>
					<select bind:value={settings.theme} class="block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100">
						<option value="light">Claro</option>
						<option value="dark">Oscuro</option>
						<option value="auto">Automático</option>
					</select>
				</div>
				<div>
					<label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
						Idioma
					</label>
					<select bind:value={settings.language} class="block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100">
						<option value="es">Español</option>
						<option value="en">English</option>
					</select>
				</div>
			</div>
		</div>

		<!-- Configuración de Notificaciones -->
		<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
			<h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
				<User class="w-5 h-5 mr-2" />
				Preferencias de Usuario
				<HelpTooltip text={help.getTooltipText('settings.preferences')}>
					<HelpIcon helpKey="settings.preferences" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</h3>
			<div class="space-y-4">
				<div class="flex items-center justify-between">
					<div>
						<h3 class="text-sm font-medium text-gray-900 dark:text-white">Notificaciones del sistema</h3>
						<p class="text-sm text-gray-500 dark:text-gray-400">Recibe notificaciones sobre el estado de las tareas</p>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input type="checkbox" bind:checked={settings.notifications} class="sr-only peer">
						<div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
					</label>
				</div>
			</div>
		</div>

		<!-- Configuración de Proyectos -->
		<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
			<h2 class="text-lg font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
				<Database class="w-5 h-5 mr-2" />
				Proyectos
			</h2>
			<div class="space-y-4">
				<div>
					<label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
						Ruta de proyectos
					</label>
					<input 
						type="text" 
						bind:value={settings.projectPath}
						class="block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100"
						placeholder="/ruta/a/proyectos"
					>
				</div>
				<div class="flex items-center justify-between">
					<div>
						<h3 class="text-sm font-medium text-gray-900 dark:text-white">Guardado automático</h3>
						<p class="text-sm text-gray-500 dark:text-gray-400">Guarda automáticamente los cambios cada 30 segundos</p>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input type="checkbox" bind:checked={settings.autoSave} class="sr-only peer">
						<div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
					</label>
				</div>
			</div>
		</div>

		<!-- Gestión de Templates -->
		<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
			<h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
				<FileText class="w-5 h-5 mr-2" />
				Gestión de Templates
				<HelpTooltip text={help.getTooltipText('settings.templates')}>
					<HelpIcon helpKey="settings.templates" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</h3>
			<div class="space-y-4">
				<p class="text-gray-600 dark:text-gray-400">
					Administra y personaliza los templates de sesiones de trabajo.
				</p>
				<div class="flex space-x-3">
					<button class="mighty-button-secondary">
						<Plus class="w-4 h-4 mr-2" />
						Nuevo Template
					</button>
					<button class="mighty-button-secondary">
						<Upload class="w-4 h-4 mr-2" />
						Importar Template
					</button>
				</div>
			</div>
		</div>

		<!-- Configuración de Seguridad -->
		<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
			<h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
				<Shield class="w-5 h-5 mr-2" />
				Seguridad y Respaldos
			</h3>
			<div class="space-y-4">
				<div class="flex items-center justify-between">
					<div>
						<h3 class="text-sm font-medium text-gray-900 dark:text-white">Respaldos automáticos</h3>
						<p class="text-sm text-gray-500 dark:text-gray-400">Crear respaldos automáticos de tus proyectos</p>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input type="checkbox" bind:checked={settings.backupEnabled} class="sr-only peer">
						<div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
					</label>
				</div>
			</div>
		</div>

		<!-- Botones de acción -->
		<div class="flex justify-end space-x-4">
			<button 
				class="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
			>
				Cancelar
			</button>
			<button 
				on:click={saveSettings}
				disabled={loading}
				class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 disabled:opacity-50 transition-colors"
			>
				{loading ? 'Guardando...' : 'Guardar Cambios'}
			</button>
		</div>
	</div>
</div>
