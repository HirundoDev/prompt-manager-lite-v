# Frontend Component Catalog & Manifest Template
> **Purpose:** Universal template for creating comprehensive frontend component catalogs following 2025 best practices for component-driven development, design systems, and modern frontend architecture. This template serves as the foundation for documenting UI components, pages, and frontend modules in any technology stack.

**Document Type:** Frontend Architecture & Component Catalog Template  
**Version:** 2.0 - Universal Template with 2025 Best Practices  
**Last Updated:** 2025-01-15  
**Template Status:** Production Ready

---

## Document Control
| Field | Value |
|-------|-------|
| **Project Name** | [PROJECT_NAME] |
| **Frontend Framework** | [FRONTEND_FRAMEWORK] |
| **UI Library** | [UI_LIBRARY] |
| **Frontend Architect** | [FRONTEND_ARCHITECT_NAME] |
| **UI/UX Lead** | [UI_UX_LEAD_NAME] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] |
| **Total Components** | [COMPONENT_COUNT] |

---

## 📋 Table of Contents
- [🎯 Component Catalog Overview](#-component-catalog-overview)
- [🏗️ Frontend Architecture](#️-frontend-architecture)
- [🧩 Design System Components](#-design-system-components)
- [📱 Application Pages & Views](#-application-pages--views)
- [🔧 Utility Components & Hooks](#-utility-components--hooks)
- [🎨 Styling & Theme System](#-styling--theme-system)
- [📊 State Management](#-state-management)
- [🔄 Data Fetching & API Integration](#-data-fetching--api-integration)
- [🧪 Testing & Quality Assurance](#-testing--quality-assurance)
- [📚 Documentation & Storybook](#-documentation--storybook)
- [🚀 Build System & Performance](#-build-system--performance)
- [🎯 Component Standards & Guidelines](#-component-standards--guidelines)

---

## 🎯 Component Catalog Overview

### Component-Driven Development Philosophy

Our frontend architecture follows modern component-driven development principles, emphasizing reusability, maintainability, and scalability:

#### 🔍 **Component Discovery & Organization**
- **Atomic Design methodology** with atoms, molecules, organisms, templates, and pages
- **Design system integration** with Storybook for component documentation
- **Component library** with versioned, reusable UI components
- **Pattern library** documenting common interaction patterns and layouts

#### 🎨 **Design System Integration**
- **Design tokens** for consistent spacing, colors, typography, and animations
- **Component variants** supporting different sizes, states, and themes
- **Accessibility standards** built into every component (WCAG 2.1 AA)
- **Responsive design** with mobile-first approach and breakpoint system

#### 📊 **Performance & Optimization**
- **Code splitting** at component and route levels
- **Lazy loading** for non-critical components and images
- **Bundle optimization** with tree shaking and dead code elimination
- **Runtime performance** monitoring with Core Web Vitals tracking

### Component Classification

Our components are organized by complexity and purpose:

#### **Component Hierarchy**
- **Atoms:** Basic building blocks (buttons, inputs, icons)
- **Molecules:** Simple combinations of atoms (search box, card header)
- **Organisms:** Complex UI sections (navigation, product grid)
- **Templates:** Page-level layouts without specific content
- **Pages:** Complete views with real content and data

#### **Component Categories**
- **Design System:** Foundational UI components following design standards
- **Business Logic:** Domain-specific components with business rules
- **Layout:** Structural components for page organization
- **Interactive:** Components with complex user interactions
- **Data Display:** Components for presenting and visualizing data

---#
# 🏗️ Frontend Architecture

### Technology Stack Overview

Document your frontend architecture and technology choices:

#### **Core Framework Stack**
```yaml
runtime: [RUNTIME_ENVIRONMENT]
framework: [FRONTEND_FRAMEWORK]
ui_library: [UI_LIBRARY]
language: [PROGRAMMING_LANGUAGE]
styling: [STYLING_SOLUTION]
state_management: [STATE_MANAGEMENT_SOLUTION]
forms: [FORM_HANDLING_LIBRARY]
testing: [TESTING_FRAMEWORKS]
documentation: [DOCUMENTATION_TOOL]
```

#### **Build and Development Tools**
```yaml
bundler: [BUILD_TOOL]
package_manager: [PACKAGE_MANAGER]
linting: [LINTING_TOOLS]
formatting: [CODE_FORMATTING]
pre_commit: [PRE_COMMIT_HOOKS]
ci_cd: [CI_CD_PLATFORM]
deployment: [DEPLOYMENT_PLATFORM]
monitoring: [MONITORING_TOOLS]
```

#### **Architecture Patterns**
Document the rendering and architectural patterns used in your project:
- **[RENDERING_PATTERN_1]** - [Description and use case]
- **[RENDERING_PATTERN_2]** - [Description and use case]
- **[RENDERING_PATTERN_3]** - [Description and use case]
- **[ADDITIONAL_PATTERNS]** - [Description and use case]

### Project Structure

Document your frontend project structure (adapt to your framework):

```
[PROJECT_ROOT]/
├── [PAGES_DIRECTORY]/          # Pages/routes directory
│   ├── [ROUTE_GROUP_1]/       # Route grouping (if applicable)
│   ├── [ROUTE_GROUP_2]/       # Route grouping (if applicable)
│   ├── [GLOBAL_STYLES]        # Global styles
│   ├── [ROOT_LAYOUT]          # Root layout component
│   └── [HOME_PAGE]            # Home page component
├── [COMPONENTS_DIRECTORY]/     # Reusable UI components
│   ├── [UI_COMPONENTS]/       # Design system components
│   ├── [FORM_COMPONENTS]/     # Form-specific components
│   ├── [LAYOUT_COMPONENTS]/   # Layout and navigation components
│   └── [FEATURE_COMPONENTS]/  # Feature-specific components
├── [UTILITIES_DIRECTORY]/      # Utility functions and configurations
│   ├── [UTILS_FILE]           # General utility functions
│   ├── [VALIDATIONS_FILE]     # Validation schemas
│   ├── [API_CLIENT]           # API client configuration
│   └── [AUTH_UTILITIES]       # Authentication utilities
├── [HOOKS_DIRECTORY]/          # Custom hooks (if applicable)
├── [STATE_DIRECTORY]/          # State management files
├── [TYPES_DIRECTORY]/          # Type definitions
└── [STYLES_DIRECTORY]/         # Additional styles and themes
```

---#
# 🧩 Design System Components

### Atomic Design System

Our component library follows atomic design principles for maximum reusability and consistency:

#### **Atoms - Basic Building Blocks**

##### **Button Component Example**
```[PROGRAMMING_LANGUAGE]
// [COMPONENT_PATH]/button.[FILE_EXTENSION]
interface ButtonProps {
  variant: [VARIANT_OPTIONS]
  size: [SIZE_OPTIONS]
  loading?: boolean
  disabled?: boolean
  children: [CHILDREN_TYPE]
  onClick?: [CLICK_HANDLER_TYPE]
}

const Button: [COMPONENT_TYPE] = ({
  variant = '[DEFAULT_VARIANT]',
  size = '[DEFAULT_SIZE]',
  loading = false,
  disabled = false,
  children,
  onClick,
  ...props
}) => {
  return (
    [COMPONENT_MARKUP_WITH_STYLING]
  )
}
```
```

**Component Metadata Template:**
```yaml
component_name: [COMPONENT_NAME]
category: [ATOMIC_DESIGN_LEVEL] # atoms/molecules/organisms
design_tokens:
  - [DESIGN_TOKEN_1] ([TOKEN_VALUES])
  - [DESIGN_TOKEN_2] ([TOKEN_VALUES])
  - [DESIGN_TOKEN_3] ([TOKEN_VALUES])
  - [ADDITIONAL_TOKENS]
accessibility:
  - [ACCESSIBILITY_FEATURE_1]
  - [ACCESSIBILITY_FEATURE_2]
  - [ACCESSIBILITY_FEATURE_3]
  - [ADDITIONAL_A11Y_FEATURES]
variants:
  - [VARIANT_1]: [VARIANT_DESCRIPTION]
  - [VARIANT_2]: [VARIANT_DESCRIPTION]
  - [VARIANT_3]: [VARIANT_DESCRIPTION]
  - [ADDITIONAL_VARIANTS]: [DESCRIPTIONS]
states:
  - [STATE_1], [STATE_2], [STATE_3], [ADDITIONAL_STATES]
```

##### **Input Component**
```typescript
// components/ui/input.tsx
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
  helperText?: string
  leftIcon?: React.ReactNode
  rightIcon?: React.ReactNode
  variant: 'default' | 'filled' | 'outline'
}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, helperText, leftIcon, rightIcon, variant = 'default', className, ...props }, ref) => {
    return (
      <div className="space-y-2">
        {label && (
          <label className="text-sm font-medium text-gray-700">
            {label}
          </label>
        )}
        <div className="relative">
          {leftIcon && (
            <div className="absolute left-3 top-1/2 -translate-y-1/2">
              {leftIcon}
            </div>
          )}
          <input
            ref={ref}
            className={cn(
              inputVariants({ variant }),
              leftIcon && 'pl-10',
              rightIcon && 'pr-10',
              error && 'border-red-500 focus:border-red-500',
              className
            )}
            {...props}
          />
          {rightIcon && (
            <div className="absolute right-3 top-1/2 -translate-y-1/2">
              {rightIcon}
            </div>
          )}
        </div>
        {error && (
          <p className="text-sm text-red-600">{error}</p>
        )}
        {helperText && !error && (
          <p className="text-sm text-gray-500">{helperText}</p>
        )}
      </div>
    )
  }
)
```

---#### **
Molecules - Component Combinations**

##### **Search Box Component**
```typescript
// components/ui/search-box.tsx
interface SearchBoxProps {
  placeholder?: string
  onSearch: (query: string) => void
  suggestions?: string[]
  loading?: boolean
  debounceMs?: number
}

const SearchBox: React.FC<SearchBoxProps> = ({
  placeholder = "Search...",
  onSearch,
  suggestions = [],
  loading = false,
  debounceMs = 300
}) => {
  const [query, setQuery] = useState('')
  const [showSuggestions, setShowSuggestions] = useState(false)
  const debouncedQuery = useDebounce(query, debounceMs)

  useEffect(() => {
    if (debouncedQuery) {
      onSearch(debouncedQuery)
    }
  }, [debouncedQuery, onSearch])

  return (
    <div className="relative w-full max-w-md">
      <Input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder={placeholder}
        leftIcon={<SearchIcon className="h-4 w-4 text-gray-400" />}
        rightIcon={loading && <Spinner className="h-4 w-4" />}
        onFocus={() => setShowSuggestions(true)}
        onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
      />
      
      {showSuggestions && suggestions.length > 0 && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-white border border-gray-200 rounded-md shadow-lg z-50">
          {suggestions.map((suggestion, index) => (
            <button
              key={index}
              className="w-full px-4 py-2 text-left hover:bg-gray-50 first:rounded-t-md last:rounded-b-md"
              onClick={() => {
                setQuery(suggestion)
                onSearch(suggestion)
                setShowSuggestions(false)
              }}
            >
              {suggestion}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}
```

##### **Card Component**
```typescript
// components/ui/card.tsx
interface CardProps {
  children: React.ReactNode
  variant?: 'default' | 'outlined' | 'elevated'
  padding?: 'none' | 'sm' | 'md' | 'lg'
  className?: string
}

const Card: React.FC<CardProps> = ({
  children,
  variant = 'default',
  padding = 'md',
  className
}) => {
  return (
    <div
      className={cn(
        cardVariants({ variant, padding }),
        className
      )}
    >
      {children}
    </div>
  )
}

const CardHeader: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div className="border-b border-gray-200 px-6 py-4">
    {children}
  </div>
)

const CardContent: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div className="px-6 py-4">
    {children}
  </div>
)

const CardFooter: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div className="border-t border-gray-200 px-6 py-4">
    {children}
  </div>
)

Card.Header = CardHeader
Card.Content = CardContent
Card.Footer = CardFooter
```

---#### **Or
ganisms - Complex UI Sections**

##### **Navigation Component**
```typescript
// components/layout/navigation.tsx
interface NavigationItem {
  label: string
  href: string
  icon?: React.ReactNode
  badge?: string | number
  children?: NavigationItem[]
}

interface NavigationProps {
  items: NavigationItem[]
  currentPath: string
  onItemClick?: (item: NavigationItem) => void
}

const Navigation: React.FC<NavigationProps> = ({
  items,
  currentPath,
  onItemClick
}) => {
  return (
    <nav className="space-y-1">
      {items.map((item) => (
        <NavigationItem
          key={item.href}
          item={item}
          currentPath={currentPath}
          onItemClick={onItemClick}
        />
      ))}
    </nav>
  )
}

const NavigationItem: React.FC<{
  item: NavigationItem
  currentPath: string
  onItemClick?: (item: NavigationItem) => void
}> = ({ item, currentPath, onItemClick }) => {
  const isActive = currentPath === item.href
  const hasChildren = item.children && item.children.length > 0
  const [isExpanded, setIsExpanded] = useState(false)

  return (
    <div>
      <Link
        href={item.href}
        className={cn(
          "flex items-center px-3 py-2 rounded-md text-sm font-medium transition-colors",
          isActive
            ? "bg-primary-100 text-primary-900"
            : "text-gray-700 hover:bg-gray-100"
        )}
        onClick={() => {
          onItemClick?.(item)
          if (hasChildren) {
            setIsExpanded(!isExpanded)
          }
        }}
      >
        {item.icon && (
          <span className="mr-3 h-5 w-5">{item.icon}</span>
        )}
        <span className="flex-1">{item.label}</span>
        {item.badge && (
          <Badge variant="secondary" className="ml-2">
            {item.badge}
          </Badge>
        )}
        {hasChildren && (
          <ChevronDownIcon
            className={cn(
              "ml-2 h-4 w-4 transition-transform",
              isExpanded && "rotate-180"
            )}
          />
        )}
      </Link>
      
      {hasChildren && isExpanded && (
        <div className="ml-6 mt-1 space-y-1">
          {item.children!.map((child) => (
            <NavigationItem
              key={child.href}
              item={child}
              currentPath={currentPath}
              onItemClick={onItemClick}
            />
          ))}
        </div>
      )}
    </div>
  )
}
```

---#
# 📱 Application Pages & Views

### Page Architecture

Our pages follow Next.js App Router conventions with server and client components:

#### **Authentication Pages**

##### **Login Page**
```typescript
// app/(auth)/login/page.tsx
import { LoginForm } from '@/components/forms/login-form'
import { AuthLayout } from '@/components/layout/auth-layout'

export default function LoginPage() {
  return (
    <AuthLayout
      title="Welcome back"
      subtitle="Sign in to your account to continue"
    >
      <LoginForm />
    </AuthLayout>
  )
}

// components/forms/login-form.tsx
'use client'

const loginSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
  rememberMe: z.boolean().optional()
})

export const LoginForm: React.FC = () => {
  const form = useForm<z.infer<typeof loginSchema>>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: '',
      password: '',
      rememberMe: false
    }
  })

  const { mutate: login, isPending } = useMutation({
    mutationFn: authApi.login,
    onSuccess: () => {
      router.push('/dashboard')
    },
    onError: (error) => {
      toast.error(error.message)
    }
  })

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(login)} className="space-y-6">
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input
                  type="email"
                  placeholder="Enter your email"
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        
        <FormField
          control={form.control}
          name="password"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Password</FormLabel>
              <FormControl>
                <Input
                  type="password"
                  placeholder="Enter your password"
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        
        <FormField
          control={form.control}
          name="rememberMe"
          render={({ field }) => (
            <FormItem className="flex items-center space-x-2">
              <FormControl>
                <Checkbox
                  checked={field.value}
                  onCheckedChange={field.onChange}
                />
              </FormControl>
              <FormLabel className="text-sm font-normal">
                Remember me
              </FormLabel>
            </FormItem>
          )}
        />
        
        <Button
          type="submit"
          className="w-full"
          loading={isPending}
        >
          Sign In
        </Button>
      </form>
    </Form>
  )
}
```

---##
## **Dashboard Pages**

##### **Dashboard Overview**
```typescript
// app/(dashboard)/dashboard/page.tsx
import { Suspense } from 'react'
import { DashboardStats } from '@/components/features/dashboard/dashboard-stats'
import { RecentActivity } from '@/components/features/dashboard/recent-activity'
import { QuickActions } from '@/components/features/dashboard/quick-actions'
import { DashboardLayout } from '@/components/layout/dashboard-layout'

export default function DashboardPage() {
  return (
    <DashboardLayout>
      <div className="space-y-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
          <p className="text-gray-600">Welcome back! Here's what's happening.</p>
        </div>
        
        <Suspense fallback={<StatsLoading />}>
          <DashboardStats />
        </Suspense>
        
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2">
            <Suspense fallback={<ActivityLoading />}>
              <RecentActivity />
            </Suspense>
          </div>
          
          <div>
            <QuickActions />
          </div>
        </div>
      </div>
    </DashboardLayout>
  )
}

// components/features/dashboard/dashboard-stats.tsx
export const DashboardStats: React.FC = async () => {
  const stats = await getDashboardStats()
  
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {stats.map((stat) => (
        <Card key={stat.id}>
          <Card.Content className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">
                  {stat.label}
                </p>
                <p className="text-2xl font-bold text-gray-900">
                  {stat.value}
                </p>
              </div>
              <div className={cn(
                "p-3 rounded-full",
                stat.trend === 'up' ? 'bg-green-100' : 'bg-red-100'
              )}>
                <stat.icon className={cn(
                  "h-6 w-6",
                  stat.trend === 'up' ? 'text-green-600' : 'text-red-600'
                )} />
              </div>
            </div>
            
            {stat.change && (
              <div className="mt-4 flex items-center">
                <span className={cn(
                  "text-sm font-medium",
                  stat.trend === 'up' ? 'text-green-600' : 'text-red-600'
                )}>
                  {stat.trend === 'up' ? '+' : '-'}{stat.change}%
                </span>
                <span className="text-sm text-gray-500 ml-2">
                  from last month
                </span>
              </div>
            )}
          </Card.Content>
        </Card>
      ))}
    </div>
  )
}
```

---## 🔧 Uti
lity Components & Hooks

### Custom Hooks Library

#### **Data Fetching Hooks**
```typescript
// hooks/use-api.ts
export const useApi = <T>(
  queryKey: string[],
  queryFn: () => Promise<T>,
  options?: UseQueryOptions<T>
) => {
  return useQuery({
    queryKey,
    queryFn,
    staleTime: 5 * 60 * 1000, // 5 minutes
    cacheTime: 10 * 60 * 1000, // 10 minutes
    ...options
  })
}

// hooks/use-pagination.ts
export const usePagination = (totalItems: number, itemsPerPage: number = 10) => {
  const [currentPage, setCurrentPage] = useState(1)
  
  const totalPages = Math.ceil(totalItems / itemsPerPage)
  const startIndex = (currentPage - 1) * itemsPerPage
  const endIndex = Math.min(startIndex + itemsPerPage, totalItems)
  
  const goToPage = (page: number) => {
    setCurrentPage(Math.max(1, Math.min(page, totalPages)))
  }
  
  const nextPage = () => goToPage(currentPage + 1)
  const prevPage = () => goToPage(currentPage - 1)
  
  return {
    currentPage,
    totalPages,
    startIndex,
    endIndex,
    goToPage,
    nextPage,
    prevPage,
    hasNextPage: currentPage < totalPages,
    hasPrevPage: currentPage > 1
  }
}

// hooks/use-debounce.ts
export const useDebounce = <T>(value: T, delay: number): T => {
  const [debouncedValue, setDebouncedValue] = useState<T>(value)
  
  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value)
    }, delay)
    
    return () => {
      clearTimeout(handler)
    }
  }, [value, delay])
  
  return debouncedValue
}
```

#### **UI State Hooks**
```typescript
// hooks/use-disclosure.ts
export const useDisclosure = (initialState: boolean = false) => {
  const [isOpen, setIsOpen] = useState(initialState)
  
  const open = useCallback(() => setIsOpen(true), [])
  const close = useCallback(() => setIsOpen(false), [])
  const toggle = useCallback(() => setIsOpen(prev => !prev), [])
  
  return { isOpen, open, close, toggle }
}

// hooks/use-local-storage.ts
export const useLocalStorage = <T>(
  key: string,
  initialValue: T
): [T, (value: T | ((val: T) => T)) => void] => {
  const [storedValue, setStoredValue] = useState<T>(() => {
    if (typeof window === 'undefined') {
      return initialValue
    }
    
    try {
      const item = window.localStorage.getItem(key)
      return item ? JSON.parse(item) : initialValue
    } catch (error) {
      console.error(`Error reading localStorage key "${key}":`, error)
      return initialValue
    }
  })
  
  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value
      setStoredValue(valueToStore)
      
      if (typeof window !== 'undefined') {
        window.localStorage.setItem(key, JSON.stringify(valueToStore))
      }
    } catch (error) {
      console.error(`Error setting localStorage key "${key}":`, error)
    }
  }
  
  return [storedValue, setValue]
}
```

---###
 Utility Components

#### **Loading States**
```typescript
// components/ui/loading.tsx
export const Spinner: React.FC<{ className?: string }> = ({ className }) => (
  <div
    className={cn(
      "animate-spin rounded-full border-2 border-gray-300 border-t-primary-600",
      className
    )}
  />
)

export const Skeleton: React.FC<{ className?: string }> = ({ className }) => (
  <div
    className={cn(
      "animate-pulse bg-gray-200 rounded",
      className
    )}
  />
)

export const LoadingCard: React.FC = () => (
  <Card>
    <Card.Content className="p-6">
      <div className="space-y-4">
        <Skeleton className="h-4 w-3/4" />
        <Skeleton className="h-4 w-1/2" />
        <Skeleton className="h-8 w-full" />
      </div>
    </Card.Content>
  </Card>
)
```

#### **Error Boundaries**
```typescript
// components/ui/error-boundary.tsx
interface ErrorBoundaryProps {
  children: React.ReactNode
  fallback?: React.ComponentType<{ error: Error; resetError: () => void }>
}

export const ErrorBoundary: React.FC<ErrorBoundaryProps> = ({
  children,
  fallback: Fallback = DefaultErrorFallback
}) => {
  return (
    <ReactErrorBoundary
      FallbackComponent={Fallback}
      onError={(error, errorInfo) => {
        console.error('Error caught by boundary:', error, errorInfo)
        // Send to error reporting service
      }}
    >
      {children}
    </ReactErrorBoundary>
  )
}

const DefaultErrorFallback: React.FC<{
  error: Error
  resetError: () => void
}> = ({ error, resetError }) => (
  <Card className="border-red-200 bg-red-50">
    <Card.Content className="p-6 text-center">
      <div className="mb-4">
        <ExclamationTriangleIcon className="mx-auto h-12 w-12 text-red-500" />
      </div>
      <h3 className="text-lg font-semibold text-red-900 mb-2">
        Something went wrong
      </h3>
      <p className="text-red-700 mb-4">
        {error.message || 'An unexpected error occurred'}
      </p>
      <Button onClick={resetError} variant="outline">
        Try again
      </Button>
    </Card.Content>
  </Card>
)
```

---##
 🎨 Styling & Theme System

### Design Token System

Our design system uses Tailwind CSS with custom design tokens for consistency:

#### **Color Palette Template**
```[CONFIGURATION_FORMAT]
// [STYLING_CONFIG_FILE]
const colors = {
  [PRIMARY_COLOR_NAME]: {
    [SHADE_1]: '[COLOR_VALUE_1]',
    [SHADE_2]: '[COLOR_VALUE_2]',
    [SHADE_3]: '[COLOR_VALUE_3]',
    // Add more shades as needed
  },
  [NEUTRAL_COLOR_NAME]: {
    [SHADE_1]: '[COLOR_VALUE_1]',
    [SHADE_2]: '[COLOR_VALUE_2]',
    [SHADE_3]: '[COLOR_VALUE_3]',
    // Add more shades as needed
  },
  [SEMANTIC_COLOR_1]: {
    [SHADE_1]: '[COLOR_VALUE_1]',
    [SHADE_2]: '[COLOR_VALUE_2]',
    [SHADE_3]: '[COLOR_VALUE_3]'
  },
  [SEMANTIC_COLOR_2]: {
    [SHADE_1]: '[COLOR_VALUE_1]',
    [SHADE_2]: '[COLOR_VALUE_2]',
    [SHADE_3]: '[COLOR_VALUE_3]'
  },
  [SEMANTIC_COLOR_3]: {
    [SHADE_1]: '[COLOR_VALUE_1]',
    [SHADE_2]: '[COLOR_VALUE_2]',
    [SHADE_3]: '[COLOR_VALUE_3]'
  }
}
```

#### **Typography Scale Template**
```[CONFIGURATION_FORMAT]
const typography = {
  fontFamily: {
    [FONT_FAMILY_1]: ['[PRIMARY_FONT]', '[FALLBACK_FONTS]'],
    [FONT_FAMILY_2]: ['[SECONDARY_FONT]', '[FALLBACK_FONTS]']
  },
  fontSize: {
    [SIZE_NAME_1]: ['[FONT_SIZE]', { lineHeight: '[LINE_HEIGHT]' }],
    [SIZE_NAME_2]: ['[FONT_SIZE]', { lineHeight: '[LINE_HEIGHT]' }],
    [SIZE_NAME_3]: ['[FONT_SIZE]', { lineHeight: '[LINE_HEIGHT]' }],
    [SIZE_NAME_4]: ['[FONT_SIZE]', { lineHeight: '[LINE_HEIGHT]' }],
    [SIZE_NAME_5]: ['[FONT_SIZE]', { lineHeight: '[LINE_HEIGHT]' }],
    [SIZE_NAME_6]: ['[FONT_SIZE]', { lineHeight: '[LINE_HEIGHT]' }],
    [SIZE_NAME_7]: ['[FONT_SIZE]', { lineHeight: '[LINE_HEIGHT]' }],
    [SIZE_NAME_8]: ['[FONT_SIZE]', { lineHeight: '[LINE_HEIGHT]' }]
  }
}
```

#### **Spacing System Template**
```[CONFIGURATION_FORMAT]
const spacing = {
  [SPACING_UNIT_1]: '[SPACING_VALUE_1]',   // [PIXEL_VALUE_1]
  [SPACING_UNIT_2]: '[SPACING_VALUE_2]',   // [PIXEL_VALUE_2]
  [SPACING_UNIT_3]: '[SPACING_VALUE_3]',   // [PIXEL_VALUE_3]
  [SPACING_UNIT_4]: '[SPACING_VALUE_4]',   // [PIXEL_VALUE_4]
  [SPACING_UNIT_5]: '[SPACING_VALUE_5]',   // [PIXEL_VALUE_5]
  [SPACING_UNIT_6]: '[SPACING_VALUE_6]',   // [PIXEL_VALUE_6]
  [SPACING_UNIT_7]: '[SPACING_VALUE_7]',   // [PIXEL_VALUE_7]
  [SPACING_UNIT_8]: '[SPACING_VALUE_8]',   // [PIXEL_VALUE_8]
  // Add more spacing units as needed
}
```

### Component Variants System

```typescript
// lib/variants.ts
import { cva, type VariantProps } from 'class-variance-authority'

export const buttonVariants = cva(
  // Base styles
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-background",
  {
    variants: {
      variant: {
        primary: "bg-primary-600 text-white hover:bg-primary-700 active:bg-primary-800",
        secondary: "bg-gray-100 text-gray-900 hover:bg-gray-200 active:bg-gray-300",
        outline: "border border-gray-300 bg-white text-gray-700 hover:bg-gray-50 active:bg-gray-100",
        ghost: "text-gray-700 hover:bg-gray-100 active:bg-gray-200",
        destructive: "bg-red-600 text-white hover:bg-red-700 active:bg-red-800"
      },
      size: {
        sm: "h-8 px-3 text-xs",
        md: "h-10 px-4 py-2",
        lg: "h-12 px-6 text-base",
        xl: "h-14 px-8 text-lg"
      }
    },
    defaultVariants: {
      variant: "primary",
      size: "md"
    }
  }
)

export type ButtonVariants = VariantProps<typeof buttonVariants>
```

---#
# 📊 State Management

### State Management Architecture

Document your state management approach and architecture:

#### **Authentication State Example**
```[PROGRAMMING_LANGUAGE]
// [STATE_DIRECTORY]/[AUTH_STORE_FILE]
interface [USER_INTERFACE] {
  [USER_ID_FIELD]: [ID_TYPE]
  [USER_EMAIL_FIELD]: [EMAIL_TYPE]
  [USER_NAME_FIELD]: [NAME_TYPE]
  [USER_AVATAR_FIELD]?: [AVATAR_TYPE]
  [USER_ROLE_FIELD]: [ROLE_TYPE]
}

interface [AUTH_STATE_INTERFACE] {
  [USER_STATE]: [USER_INTERFACE] | null
  [AUTH_STATUS]: boolean
  [LOADING_STATE]: boolean
  [LOGIN_METHOD]: ([CREDENTIALS_TYPE]) => [PROMISE_TYPE]
  [LOGOUT_METHOD]: () => void
  [UPDATE_PROFILE_METHOD]: ([UPDATE_DATA_TYPE]) => [PROMISE_TYPE]
}

export const [AUTH_STORE_NAME] = [STATE_MANAGEMENT_IMPLEMENTATION]({
  [INITIAL_STATE_DEFINITION],
  [STATE_ACTIONS_IMPLEMENTATION],
  [PERSISTENCE_CONFIGURATION] // if applicable
})
```

#### **UI State Store**
```typescript
// stores/ui-store.ts
interface UIState {
  sidebarOpen: boolean
  theme: 'light' | 'dark' | 'system'
  notifications: Notification[]
  toggleSidebar: () => void
  setTheme: (theme: 'light' | 'dark' | 'system') => void
  addNotification: (notification: Omit<Notification, 'id'>) => void
  removeNotification: (id: string) => void
}

export const useUIStore = create<UIState>()(
  devtools(
    persist(
      (set, get) => ({
        sidebarOpen: true,
        theme: 'system',
        notifications: [],

        toggleSidebar: () => {
          set((state) => ({ sidebarOpen: !state.sidebarOpen }))
        },

        setTheme: (theme) => {
          set({ theme })
          // Apply theme to document
          if (theme === 'dark' || (theme === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark')
          } else {
            document.documentElement.classList.remove('dark')
          }
        },

        addNotification: (notification) => {
          const id = Math.random().toString(36).substr(2, 9)
          const newNotification = { ...notification, id }
          set((state) => ({
            notifications: [...state.notifications, newNotification]
          }))

          // Auto-remove after 5 seconds
          setTimeout(() => {
            get().removeNotification(id)
          }, 5000)
        },

        removeNotification: (id) => {
          set((state) => ({
            notifications: state.notifications.filter(n => n.id !== id)
          }))
        }
      }),
      {
        name: 'ui-storage',
        partialize: (state) => ({ 
          sidebarOpen: state.sidebarOpen, 
          theme: state.theme 
        })
      }
    )
  )
)
```

---## 🔄 D
ata Fetching & API Integration

### Data Fetching & API Integration

#### **API Client Configuration Template**
```[PROGRAMMING_LANGUAGE]
// [UTILITIES_DIRECTORY]/[API_CLIENT_FILE]
import [HTTP_CLIENT_LIBRARY] from '[HTTP_CLIENT_PACKAGE]'

const [API_CLIENT_NAME] = [HTTP_CLIENT_LIBRARY].[CREATE_METHOD]({
  [BASE_URL_CONFIG]: [API_BASE_URL],
  [TIMEOUT_CONFIG]: [TIMEOUT_VALUE],
  [HEADERS_CONFIG]: {
    '[CONTENT_TYPE_HEADER]': '[CONTENT_TYPE_VALUE]'
  }
})

// Request interceptor for authentication
[API_CLIENT_NAME].[REQUEST_INTERCEPTOR].[USE_METHOD](
  ([CONFIG_PARAM]) => {
    const [TOKEN_VARIABLE] = [TOKEN_STORAGE].[GET_METHOD]('[TOKEN_KEY]')
    if ([TOKEN_VARIABLE]) {
      [CONFIG_PARAM].[HEADERS_PROPERTY].[AUTH_HEADER] = `[AUTH_SCHEME] ${[TOKEN_VARIABLE]}`
    }
    return [CONFIG_PARAM]
  },
  ([ERROR_PARAM]) => [PROMISE_REJECTION]([ERROR_PARAM])
)

// Response interceptor for error handling
[API_CLIENT_NAME].[RESPONSE_INTERCEPTOR].[USE_METHOD](
  ([RESPONSE_PARAM]) => [RESPONSE_PARAM],
  ([ERROR_PARAM]) => {
    if ([ERROR_PARAM].[RESPONSE_PROPERTY]?.[STATUS_PROPERTY] === [UNAUTHORIZED_STATUS]) {
      // Handle unauthorized access
      [REDIRECT_TO_LOGIN]
    }
    return [PROMISE_REJECTION]([ERROR_PARAM])
  }
)

export { [API_CLIENT_NAME] }
```

#### **Query Hooks**
```typescript
// hooks/queries/use-users.ts
export const useUsers = (params?: UserQueryParams) => {
  return useQuery({
    queryKey: ['users', params],
    queryFn: () => userApi.getUsers(params),
    staleTime: 5 * 60 * 1000, // 5 minutes
    cacheTime: 10 * 60 * 1000 // 10 minutes
  })
}

export const useUser = (id: string) => {
  return useQuery({
    queryKey: ['users', id],
    queryFn: () => userApi.getUser(id),
    enabled: !!id
  })
}

export const useCreateUser = () => {
  const queryClient = useQueryClient()
  
  return useMutation({
    mutationFn: userApi.createUser,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] })
      toast.success('User created successfully')
    },
    onError: (error) => {
      toast.error(error.message)
    }
  })
}

export const useUpdateUser = () => {
  const queryClient = useQueryClient()
  
  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: UpdateUserData }) =>
      userApi.updateUser(id, data),
    onSuccess: (updatedUser) => {
      queryClient.setQueryData(['users', updatedUser.id], updatedUser)
      queryClient.invalidateQueries({ queryKey: ['users'] })
      toast.success('User updated successfully')
    },
    onError: (error) => {
      toast.error(error.message)
    }
  })
}
```

#### **Infinite Queries for Pagination**
```typescript
// hooks/queries/use-infinite-posts.ts
export const useInfinitePosts = (filters?: PostFilters) => {
  return useInfiniteQuery({
    queryKey: ['posts', 'infinite', filters],
    queryFn: ({ pageParam = 1 }) =>
      postApi.getPosts({ ...filters, page: pageParam }),
    getNextPageParam: (lastPage) => {
      return lastPage.hasNextPage ? lastPage.page + 1 : undefined
    },
    staleTime: 5 * 60 * 1000
  })
}

// Usage in component
const PostList: React.FC = () => {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
    isLoading,
    error
  } = useInfinitePosts()

  if (isLoading) return <PostListSkeleton />
  if (error) return <ErrorMessage error={error} />

  const posts = data?.pages.flatMap(page => page.data) ?? []

  return (
    <div className="space-y-4">
      {posts.map((post) => (
        <PostCard key={post.id} post={post} />
      ))}
      
      {hasNextPage && (
        <Button
          onClick={() => fetchNextPage()}
          loading={isFetchingNextPage}
          variant="outline"
          className="w-full"
        >
          Load More
        </Button>
      )}
    </div>
  )
}
```

---## 🧪 Te
sting & Quality Assurance

### Testing Strategy

#### **Unit Testing Template**
```[PROGRAMMING_LANGUAGE]
// [COMPONENT_PATH]/[COMPONENT_NAME].[TEST_FILE_EXTENSION]
import { [TESTING_UTILITIES] } from '[TESTING_LIBRARY]'
import { [COMPONENT_NAME] } from './[COMPONENT_FILE]'

[TEST_SUITE_FUNCTION]('[COMPONENT_NAME] Component', () => {
  [TEST_FUNCTION]('renders with correct text', () => {
    [RENDER_FUNCTION]([COMPONENT_JSX])
    [EXPECT_FUNCTION]([QUERY_FUNCTION]('[SELECTOR]')).toBeInTheDocument()
  })

  [TEST_FUNCTION]('handles [EVENT_TYPE] events', () => {
    const [MOCK_HANDLER] = [MOCK_FUNCTION]()
    [RENDER_FUNCTION]([COMPONENT_WITH_HANDLER])
    
    [FIRE_EVENT_FUNCTION].[EVENT_TYPE]([QUERY_FUNCTION]('[SELECTOR]'))
    [EXPECT_FUNCTION]([MOCK_HANDLER]).toHaveBeenCalledTimes(1)
  })

  [TEST_FUNCTION]('shows [STATE_NAME] state', () => {
    [RENDER_FUNCTION]([COMPONENT_WITH_STATE])
    
    const [ELEMENT_VARIABLE] = [QUERY_FUNCTION]('[SELECTOR]')
    [EXPECT_FUNCTION]([ELEMENT_VARIABLE]).toBeDisabled()
    [EXPECT_FUNCTION]([QUERY_FUNCTION]('[STATE_INDICATOR]')).toBeInTheDocument()
  })

  [TEST_FUNCTION]('applies correct [VARIANT_TYPE] classes', () => {
    [RENDER_FUNCTION]([COMPONENT_WITH_VARIANT])
    
    const [ELEMENT_VARIABLE] = [QUERY_FUNCTION]('[SELECTOR]')
    [EXPECT_FUNCTION]([ELEMENT_VARIABLE]).toHaveClass('[EXPECTED_CLASS]')
  })
})
```

#### **Integration Testing**
```typescript
// components/forms/login-form.test.tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { LoginForm } from './login-form'

const createTestQueryClient = () => new QueryClient({
  defaultOptions: {
    queries: { retry: false },
    mutations: { retry: false }
  }
})

const renderWithProviders = (component: React.ReactElement) => {
  const queryClient = createTestQueryClient()
  return render(
    <QueryClientProvider client={queryClient}>
      {component}
    </QueryClientProvider>
  )
}

describe('LoginForm', () => {
  it('submits form with valid data', async () => {
    const mockLogin = vi.fn().mockResolvedValue({ user: { id: '1' } })
    vi.mocked(authApi.login).mockImplementation(mockLogin)

    renderWithProviders(<LoginForm />)

    fireEvent.change(screen.getByLabelText(/email/i), {
      target: { value: 'test@example.com' }
    })
    fireEvent.change(screen.getByLabelText(/password/i), {
      target: { value: 'password123' }
    })

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }))

    await waitFor(() => {
      expect(mockLogin).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123',
        rememberMe: false
      })
    })
  })

  it('shows validation errors for invalid data', async () => {
    renderWithProviders(<LoginForm />)

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }))

    await waitFor(() => {
      expect(screen.getByText(/invalid email address/i)).toBeInTheDocument()
      expect(screen.getByText(/password must be at least 8 characters/i)).toBeInTheDocument()
    })
  })
})
```

#### **E2E Testing with Playwright**
```typescript
// tests/e2e/auth.spec.ts
import { test, expect } from '@playwright/test'

test.describe('Authentication Flow', () => {
  test('user can login successfully', async ({ page }) => {
    await page.goto('/login')

    await page.fill('[data-testid="email-input"]', 'test@example.com')
    await page.fill('[data-testid="password-input"]', 'password123')
    await page.click('[data-testid="login-button"]')

    await expect(page).toHaveURL('/dashboard')
    await expect(page.locator('[data-testid="user-menu"]')).toBeVisible()
  })

  test('shows error for invalid credentials', async ({ page }) => {
    await page.goto('/login')

    await page.fill('[data-testid="email-input"]', 'invalid@example.com')
    await page.fill('[data-testid="password-input"]', 'wrongpassword')
    await page.click('[data-testid="login-button"]')

    await expect(page.locator('[data-testid="error-message"]')).toContainText(
      'Invalid credentials'
    )
  })

  test('user can logout', async ({ page }) => {
    // Login first
    await page.goto('/login')
    await page.fill('[data-testid="email-input"]', 'test@example.com')
    await page.fill('[data-testid="password-input"]', 'password123')
    await page.click('[data-testid="login-button"]')

    // Then logout
    await page.click('[data-testid="user-menu"]')
    await page.click('[data-testid="logout-button"]')

    await expect(page).toHaveURL('/login')
  })
})
```

---## 📚 D
ocumentation & Storybook

### Storybook Configuration

#### **Component Stories**
```typescript
// components/ui/button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react'
import { Button } from './button'

const meta: Meta<typeof Button> = {
  title: 'UI/Button',
  component: Button,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: 'A versatile button component with multiple variants and states.'
      }
    }
  },
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'outline', 'ghost', 'destructive']
    },
    size: {
      control: 'select',
      options: ['sm', 'md', 'lg', 'xl']
    },
    loading: {
      control: 'boolean'
    },
    disabled: {
      control: 'boolean'
    }
  }
}

export default meta
type Story = StoryObj<typeof meta>

export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Primary Button'
  }
}

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Secondary Button'
  }
}

export const Loading: Story = {
  args: {
    variant: 'primary',
    loading: true,
    children: 'Loading...'
  }
}

export const AllVariants: Story = {
  render: () => (
    <div className="flex gap-4 flex-wrap">
      <Button variant="primary">Primary</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="outline">Outline</Button>
      <Button variant="ghost">Ghost</Button>
      <Button variant="destructive">Destructive</Button>
    </div>
  )
}

export const AllSizes: Story = {
  render: () => (
    <div className="flex gap-4 items-center">
      <Button size="sm">Small</Button>
      <Button size="md">Medium</Button>
      <Button size="lg">Large</Button>
      <Button size="xl">Extra Large</Button>
    </div>
  )
}
```

#### **MDX Documentation**
```mdx
<!-- components/ui/button.mdx -->
import { Canvas, Meta, Story, ArgsTable } from '@storybook/blocks'
import { Button } from './button'
import * as ButtonStories from './button.stories'

<Meta of={ButtonStories} />

# Button Component

The Button component is a fundamental UI element that triggers actions when clicked. It supports multiple variants, sizes, and states to accommodate different use cases throughout the application.

## Usage

```tsx
import { Button } from '@/components/ui/button'

function MyComponent() {
  return (
    <Button variant="primary" size="md" onClick={() => console.log('Clicked!')}>
      Click me
    </Button>
  )
}
```

## Variants

<Canvas of={ButtonStories.AllVariants} />

- **Primary**: Use for the main call-to-action on a page
- **Secondary**: Use for secondary actions that support the primary action
- **Outline**: Use for actions that need less emphasis but more than ghost buttons
- **Ghost**: Use for subtle actions or when you need minimal visual weight
- **Destructive**: Use for dangerous actions like delete or remove

## Sizes

<Canvas of={ButtonStories.AllSizes} />

Choose the appropriate size based on the context and hierarchy of your interface.

## States

### Loading State
<Canvas of={ButtonStories.Loading} />

Use the loading state to provide feedback during asynchronous operations.

### Disabled State
Disabled buttons prevent user interaction and should be used when an action is temporarily unavailable.

## Accessibility

- All buttons include proper ARIA attributes
- Keyboard navigation is fully supported
- Focus indicators meet WCAG 2.1 AA standards
- Loading states are announced to screen readers

## Best Practices

- Use clear, action-oriented labels
- Maintain consistent button hierarchy throughout your interface
- Provide loading states for actions that take time
- Use destructive variant sparingly and only for irreversible actions
```

---#
# 🚀 Build System & Performance

### Next.js Configuration

#### **Production Optimization**
```typescript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable experimental features
  experimental: {
    turbo: {
      rules: {
        '*.svg': {
          loaders: ['@svgr/webpack'],
          as: '*.js'
        }
      }
    },
    serverComponentsExternalPackages: ['@prisma/client']
  },

  // Image optimization
  images: {
    domains: ['example.com', 'cdn.example.com'],
    formats: ['image/webp', 'image/avif'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384]
  },

  // Bundle analyzer
  webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
    // Bundle analyzer in development
    if (process.env.ANALYZE === 'true') {
      const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer')
      config.plugins.push(
        new BundleAnalyzerPlugin({
          analyzerMode: 'server',
          openAnalyzer: true
        })
      )
    }

    // SVG handling
    config.module.rules.push({
      test: /\.svg$/i,
      issuer: /\.[jt]sx?$/,
      use: ['@svgr/webpack']
    })

    return config
  },

  // Headers for security and performance
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY'
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff'
          },
          {
            key: 'Referrer-Policy',
            value: 'origin-when-cross-origin'
          }
        ]
      }
    ]
  },

  // Redirects
  async redirects() {
    return [
      {
        source: '/home',
        destination: '/',
        permanent: true
      }
    ]
  }
}

module.exports = nextConfig
```

#### **Performance Monitoring**
```typescript
// lib/performance.ts
export const reportWebVitals = (metric: any) => {
  // Log to console in development
  if (process.env.NODE_ENV === 'development') {
    console.log(metric)
  }

  // Send to analytics in production
  if (process.env.NODE_ENV === 'production') {
    // Send to Vercel Analytics
    if (window.va) {
      window.va('track', 'Web Vitals', {
        name: metric.name,
        value: metric.value,
        id: metric.id
      })
    }

    // Send to custom analytics
    fetch('/api/analytics/web-vitals', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(metric)
    }).catch(console.error)
  }
}

// Usage in _app.tsx
export { reportWebVitals }
```

### Code Splitting Strategy

#### **Route-based Splitting**
```typescript
// Automatic with Next.js App Router
// Each page in app/ directory is automatically code-split

// Manual dynamic imports for heavy components
const HeavyChart = dynamic(() => import('@/components/charts/heavy-chart'), {
  loading: () => <ChartSkeleton />,
  ssr: false // Client-side only if needed
})

const ConditionalComponent = dynamic(
  () => import('@/components/conditional-component'),
  {
    loading: () => <Skeleton className="h-32 w-full" />
  }
)
```

#### **Bundle Analysis**
```bash
# Analyze bundle size
npm run build
ANALYZE=true npm run build

# Check bundle composition
npx @next/bundle-analyzer
```

---## 🎯 Comp
onent Standards & Guidelines

### Development Standards

#### **Component Creation Checklist**
- [ ] **TypeScript interfaces** defined for all props
- [ ] **Default props** specified where appropriate
- [ ] **Accessibility attributes** included (ARIA labels, roles)
- [ ] **Responsive design** implemented with mobile-first approach
- [ ] **Error boundaries** implemented for complex components
- [ ] **Loading states** handled gracefully
- [ ] **Storybook stories** created with all variants
- [ ] **Unit tests** written with good coverage
- [ ] **Documentation** updated in Storybook and README

#### **Naming Conventions**
```typescript
// Component files: PascalCase
Button.tsx
UserProfile.tsx
NavigationMenu.tsx

// Hook files: camelCase with 'use' prefix
useAuth.ts
useLocalStorage.ts
useDebounce.ts

// Utility files: camelCase
formatDate.ts
validateEmail.ts
apiClient.ts

// Type files: PascalCase with descriptive names
UserTypes.ts
ApiTypes.ts
ComponentTypes.ts
```

#### **File Organization**
```
components/
├── ui/                 # Design system components
│   ├── button/
│   │   ├── button.tsx
│   │   ├── button.test.tsx
│   │   ├── button.stories.tsx
│   │   └── index.ts
│   └── input/
│       ├── input.tsx
│       ├── input.test.tsx
│       ├── input.stories.tsx
│       └── index.ts
├── forms/             # Form-specific components
├── layout/            # Layout components
└── features/          # Feature-specific components
    └── dashboard/
        ├── dashboard-stats.tsx
        ├── dashboard-stats.test.tsx
        └── index.ts
```

### Accessibility Standards

#### **WCAG 2.1 AA Compliance**
```typescript
// Example: Accessible button component
const AccessibleButton: React.FC<ButtonProps> = ({
  children,
  onClick,
  disabled = false,
  ariaLabel,
  ariaDescribedBy,
  ...props
}) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      aria-label={ariaLabel}
      aria-describedby={ariaDescribedBy}
      className={cn(
        "focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2",
        "transition-colors duration-200",
        disabled && "opacity-50 cursor-not-allowed"
      )}
      {...props}
    >
      {children}
    </button>
  )
}
```

#### **Keyboard Navigation**
```typescript
// Example: Accessible dropdown menu
const DropdownMenu: React.FC<DropdownProps> = ({ items, trigger }) => {
  const [isOpen, setIsOpen] = useState(false)
  const [focusedIndex, setFocusedIndex] = useState(-1)

  const handleKeyDown = (event: React.KeyboardEvent) => {
    switch (event.key) {
      case 'Escape':
        setIsOpen(false)
        setFocusedIndex(-1)
        break
      case 'ArrowDown':
        event.preventDefault()
        setFocusedIndex(prev => 
          prev < items.length - 1 ? prev + 1 : 0
        )
        break
      case 'ArrowUp':
        event.preventDefault()
        setFocusedIndex(prev => 
          prev > 0 ? prev - 1 : items.length - 1
        )
        break
      case 'Enter':
      case ' ':
        if (focusedIndex >= 0) {
          items[focusedIndex].onClick()
          setIsOpen(false)
        }
        break
    }
  }

  return (
    <div className="relative" onKeyDown={handleKeyDown}>
      {/* Implementation */}
    </div>
  )
}
```

### Performance Guidelines

#### **Component Optimization**
```typescript
// Use React.memo for expensive components
const ExpensiveComponent = React.memo<Props>(({ data, onUpdate }) => {
  // Expensive rendering logic
  return <div>{/* Complex UI */}</div>
}, (prevProps, nextProps) => {
  // Custom comparison function
  return prevProps.data.id === nextProps.data.id
})

// Use useMemo for expensive calculations
const ProcessedData = ({ rawData }: { rawData: DataItem[] }) => {
  const processedData = useMemo(() => {
    return rawData
      .filter(item => item.active)
      .sort((a, b) => a.priority - b.priority)
      .map(item => ({
        ...item,
        displayName: `${item.name} (${item.category})`
      }))
  }, [rawData])

  return <DataList data={processedData} />
}

// Use useCallback for event handlers
const InteractiveComponent = ({ onSave, data }: Props) => {
  const handleSave = useCallback((formData: FormData) => {
    onSave({ ...data, ...formData })
  }, [onSave, data])

  return <Form onSubmit={handleSave} />
}
```

---

## 🔧 Quick Reference

### Component Library
- **Storybook:** [STORYBOOK_URL]
- **Design System:** [DESIGN_SYSTEM_URL]
- **Component Documentation:** [COMPONENT_DOCS_URL]
- **Figma Design Files:** [FIGMA_URL]

### Development Tools
- **Local Development:** `npm run dev`
- **Storybook:** `npm run storybook`
- **Testing:** `npm run test`
- **Build:** `npm run build`
- **Type Check:** `npm run type-check`

### Key Contacts
- **Frontend Architect:** [FRONTEND_ARCHITECT_CONTACT]
- **UI/UX Lead:** [UI_UX_LEAD_CONTACT]
- **Design System Maintainer:** [DESIGN_SYSTEM_CONTACT]
- **Frontend Team Lead:** [FRONTEND_TEAM_LEAD_CONTACT]

### Documentation Links
- **Component Guidelines:** [COMPONENT_GUIDELINES_URL]
- **Design Tokens:** [DESIGN_TOKENS_URL]
- **Accessibility Guide:** [ACCESSIBILITY_GUIDE_URL]
- **Performance Best Practices:** [PERFORMANCE_GUIDE_URL]

---

*This frontend component catalog is a living document that evolves with our design system and serves as the authoritative source for all UI components, patterns, and frontend development standards.*

---

**Last Updated:** [TIMESTAMP]  
**Next Review:** [NEXT_REVIEW_DATE]  
**Document Owner:** [FRONTEND_ARCHITECT]  
**Feedback:** [FEEDBACK_EMAIL]