<script>
	import { onMount } from 'svelte';
	import { 
		FolderOpen, 
		Plus, 
		Download, 
		Upload, 
		Search,
		MoreVertical,
		Calendar,
		Tag,
		ExternalLink,
		Trash2,
		Edit3
	} from 'lucide-svelte';
	import { getContext } from 'svelte';
	import HelpIcon from '$lib/components/HelpIcon.svelte';
	import HelpTooltip from '$lib/components/HelpTooltip.svelte';
	
	import { ProjectManager, NotificationUtils, FormatUtils } from '$lib/utils/tauri.js';
	
	// Contexto de ayuda
	const help = getContext('help');
	
	// Estado de la página
	let projects = [];
	let currentProject = null;
	let loading = true;
	let searchQuery = '';
	let showCreateModal = false;
	let selectedProject = null;
	let showProjectMenu = null;
	
	// Filtros
	let filterBy = 'all'; // all, active, inactive
	let sortBy = 'name'; // name, created, modified
	
	onMount(async () => {
		await loadProjects();
		await loadCurrentProject();
	});
	
	async function loadProjects() {
		try {
			loading = true;
			projects = await ProjectManager.listProjects();
		} catch (error) {
			console.error('Error cargando proyectos:', error);
			await NotificationUtils.error('Error', 'No se pudieron cargar los proyectos');
		} finally {
			loading = false;
		}
	}
	
	async function loadCurrentProject() {
		try {
			currentProject = await ProjectManager.getCurrentProject();
		} catch (error) {
			console.error('Error cargando proyecto actual:', error);
		}
	}
	
	async function switchToProject(projectId) {
		try {
			const result = await ProjectManager.switchProject(projectId);
			if (result.success) {
				await loadCurrentProject();
				showProjectMenu = null;
			} else {
				await NotificationUtils.error('Error', 'No se pudo cambiar al proyecto');
			}
		} catch (error) {
			console.error('Error cambiando proyecto:', error);
			await NotificationUtils.error('Error', 'Error cambiando proyecto');
		}
	}
	
	async function exportProject(projectId) {
		try {
			await ProjectManager.exportProject(projectId);
			showProjectMenu = null;
		} catch (error) {
			console.error('Error exportando proyecto:', error);
			await NotificationUtils.error('Error', 'Error exportando proyecto');
		}
	}
	
	async function importProject() {
		try {
			const result = await ProjectManager.importProject();
			if (result) {
				await loadProjects();
			}
		} catch (error) {
			console.error('Error importando proyecto:', error);
			await NotificationUtils.error('Error', 'Error importando proyecto');
		}
	}
	
	function getProjectStatusColor(project) {
		if (!project.exists) return 'text-error-600 bg-error-100';
		if (currentProject && project.id === currentProject.id) return 'text-success-600 bg-success-100';
		return 'text-secondary-600 bg-secondary-100';
	}
	
	function getProjectStatusText(project) {
		if (!project.exists) return 'No encontrado';
		if (currentProject && project.id === currentProject.id) return 'Activo';
		return 'Inactivo';
	}
	
	// Filtrar y ordenar proyectos
	$: filteredProjects = projects
		.filter(project => {
			// Filtro por búsqueda
			if (searchQuery) {
				const query = searchQuery.toLowerCase();
				return project.name.toLowerCase().includes(query) ||
				       project.organization.toLowerCase().includes(query) ||
				       project.id.toLowerCase().includes(query);
			}
			return true;
		})
		.filter(project => {
			// Filtro por estado
			if (filterBy === 'active') return project.exists && currentProject && project.id === currentProject.id;
			if (filterBy === 'inactive') return project.exists && (!currentProject || project.id !== currentProject.id);
			return true;
		})
		.sort((a, b) => {
			// Ordenamiento
			switch (sortBy) {
				case 'name':
					return a.name.localeCompare(b.name);
				case 'created':
					return new Date(b.created_at) - new Date(a.created_at);
				case 'organization':
					return a.organization.localeCompare(b.organization);
				default:
					return 0;
			}
		});
</script>

<svelte:head>
	<title>Proyectos - The Mighty Task</title>
</svelte:head>

<div class="space-y-6">
	<!-- Header de la página -->
	<div class="flex items-center justify-between">
		<div>
			<h1 class="text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
				<FolderOpen class="w-8 h-8 text-primary-600" />
				Proyectos
			</h1>
			<p class="mt-2 text-gray-600 dark:text-gray-400">
				Gestiona todos tus proyectos mighty-task desde una ubicación central
			</p>
		</div>
		
		<div class="flex items-center space-x-3">
			<div class="flex items-center space-x-1">
				<button
					class="mighty-button-secondary"
					on:click={importProject}
				>
					<Upload class="w-4 h-4 mr-2" />
					Importar
				</button>
				<HelpTooltip text={help.getTooltipText('projects.import')}>
					<HelpIcon helpKey="projects.import" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
			
			<div class="flex items-center space-x-1">
				<button
					class="mighty-button-primary"
					on:click={() => showCreateModal = true}
				>
					<Plus class="w-4 h-4 mr-2" />
					Nuevo Proyecto
				</button>
				<HelpTooltip text={help.getTooltipText('projects.create')}>
					<HelpIcon helpKey="projects.create" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
		</div>
	</div>
	
	<!-- Controles de filtrado y búsqueda -->
	<div class="mighty-card">
		<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between space-y-4 sm:space-y-0">
			<!-- Búsqueda -->
			<div class="relative flex-1 max-w-md flex items-center space-x-2">
				<div class="relative flex-1">
					<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
						<Search class="w-4 h-4 text-gray-400" />
					</div>
					<input
						type="text"
						placeholder="Buscar proyectos..."
						bind:value={searchQuery}
						class="mighty-input pl-10 pr-4 py-2 w-full"
					/>
				</div>
				<HelpTooltip text={help.getTooltipText('projects.search')}>
					<HelpIcon helpKey="projects.search" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
			
			<!-- Filtros -->
			<div class="flex items-center space-x-4">
				<div class="flex items-center space-x-1">
					<select bind:value={filterBy} class="mighty-input text-sm">
						<option value="all">Todos los proyectos</option>
						<option value="active">Proyecto activo</option>
						<option value="inactive">Proyectos inactivos</option>
					</select>
					
					<select bind:value={sortBy} class="mighty-input text-sm">
						<option value="name">Ordenar por nombre</option>
						<option value="created">Ordenar por fecha</option>
						<option value="organization">Ordenar por organización</option>
					</select>
				</div>
				<HelpTooltip text={help.getTooltipText('projects.filters')}>
					<HelpIcon helpKey="projects.filters" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
		</div>
	</div>
	
	<!-- Lista de proyectos -->
	{#if loading}
		<div class="mighty-card text-center py-12">
			<div class="animate-spin w-8 h-8 border-4 border-primary-600 border-t-transparent rounded-full mx-auto mb-4"></div>
			<p class="text-gray-500 dark:text-gray-400">Cargando proyectos...</p>
		</div>
	{:else if filteredProjects.length === 0}
		<div class="mighty-card text-center py-12">
			<FolderOpen class="w-16 h-16 text-gray-400 mx-auto mb-4" />
			<h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">
				{searchQuery ? 'No se encontraron proyectos' : 'No hay proyectos'}
			</h3>
			<p class="text-gray-500 dark:text-gray-400 mb-6">
				{searchQuery 
					? 'Intenta con otros términos de búsqueda' 
					: 'Crea tu primer proyecto para comenzar'}
			</p>
			{#if !searchQuery}
				<button
					class="mighty-button-primary"
					on:click={() => showCreateModal = true}
				>
					<Plus class="w-4 h-4 mr-2" />
					Crear Primer Proyecto
				</button>
			{/if}
		</div>
	{:else}
		<div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
			{#each filteredProjects as project}
				<div class="mighty-card hover:shadow-md mighty-transition relative">
					<!-- Menú de acciones -->
					<div class="absolute top-4 right-4">
						<button
							class="p-1 rounded text-gray-400 hover:text-gray-600 dark:hover:text-gray-200"
							on:click={() => showProjectMenu = showProjectMenu === project.id ? null : project.id}
						>
							<MoreVertical class="w-4 h-4" />
						</button>
						
						{#if showProjectMenu === project.id}
							<div class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 z-10">
								<div class="p-1">
									{#if currentProject?.id !== project.id}
										<button
											class="w-full flex items-center space-x-2 px-3 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
											on:click={() => switchToProject(project.id)}
										>
											<ExternalLink class="w-4 h-4" />
											<span>Activar Proyecto</span>
										</button>
									{/if}
									
									<button
										class="w-full flex items-center space-x-2 px-3 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
										on:click={() => exportProject(project.id)}
									>
										<Download class="w-4 h-4" />
										<span>Exportar</span>
									</button>
									
									<button
										class="w-full flex items-center space-x-2 px-3 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
									>
										<Edit3 class="w-4 h-4" />
										<span>Editar</span>
									</button>
									
									<button
										class="w-full flex items-center space-x-2 px-3 py-2 text-sm text-error-600 hover:bg-error-50 dark:hover:bg-error-900/20 rounded"
									>
										<Trash2 class="w-4 h-4" />
										<span>Eliminar</span>
									</button>
								</div>
							</div>
						{/if}
					</div>
					
					<!-- Contenido del proyecto -->
					<div class="pr-8">
						<!-- Estado y nombre -->
						<div class="flex items-start justify-between mb-3">
							<div class="flex-1">
								<h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-1">
									{project.name}
								</h3>
								<p class="text-sm text-gray-500 dark:text-gray-400">
									{project.organization}
								</p>
							</div>
						</div>
						
						<!-- Estado -->
						<div class="mb-4">
							<span class="mighty-badge {getProjectStatusColor(project)}">
								{getProjectStatusText(project)}
							</span>
						</div>
						
						<!-- Descripción -->
						{#if project.description}
							<p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
								{FormatUtils.truncateText(project.description, 100)}
							</p>
						{/if}
						
						<!-- Tags -->
						{#if project.tags && project.tags.length > 0}
							<div class="flex flex-wrap gap-1 mb-4">
								{#each project.tags.slice(0, 3) as tag}
									<span class="inline-flex items-center px-2 py-1 rounded-full text-xs bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300">
										<Tag class="w-3 h-3 mr-1" />
										{tag}
									</span>
								{/each}
								{#if project.tags.length > 3}
									<span class="text-xs text-gray-500 dark:text-gray-400">
										+{project.tags.length - 3} más
									</span>
								{/if}
							</div>
						{/if}
						
						<!-- Metadatos -->
						<div class="text-xs text-gray-500 dark:text-gray-400 space-y-1">
							<div class="flex items-center">
								<Calendar class="w-3 h-3 mr-1" />
								<span>Creado: {FormatUtils.formatDate(project.created_at)}</span>
							</div>
							<div class="font-mono text-xs bg-gray-100 dark:bg-gray-800 px-2 py-1 rounded">
								{project.id}
							</div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>

<!-- Modal para crear proyecto (placeholder) -->
{#if showCreateModal}
	<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
		<div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md">
			<h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
				Crear Nuevo Proyecto
			</h3>
			<p class="text-gray-600 dark:text-gray-400 mb-6">
				Esta funcionalidad se implementará próximamente. Por ahora, usa el CLI para crear proyectos.
			</p>
			<div class="flex justify-end space-x-3">
				<button
					class="mighty-button-secondary"
					on:click={() => showCreateModal = false}
				>
					Cerrar
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	/* Estilos adicionales si son necesarios */
</style>
